"""Question selection logic: warmup, node sections, review guide."""

import random
from datetime import datetime, timezone

from app.models import (
    CheckPoint,
    KnowledgeNode,
    KnowledgeQuestion,
    NodeSection,
    ReviewGuide,
    Sentence,
    SentenceQuestion,
    TestData,
    WarmupQuestion,
)
from app.services.data_loader import DataStore


def parse_check_point(
    cp: CheckPoint,
    understanding_goals: tuple[str, ...],
) -> tuple[str, str]:
    """CheckPoint → (question, answer)。assessment の場合は goals[0] で補完。"""
    if cp.answer:
        return cp.question, cp.answer
    if understanding_goals:
        return cp.question, understanding_goals[0]
    return cp.question, ""


def _get_reference_pages(node: KnowledgeNode, book_name: str = "") -> str:
    """Extract reference pages for the given book.

    Supports both YAML format ({"pages": "p.6"}) and
    Supabase format ({"Ch01_00": "p.6"}).
    """
    if book_name:
        book_ref = node.references.get(book_name, {})
    else:
        book_ref = next(iter(node.references.values()), {})
    if not book_ref or not isinstance(book_ref, dict):
        return ""
    # YAML format: {"section": "Ch01_00", "pages": "p.6"}
    if "pages" in book_ref:
        return book_ref["pages"]
    # Supabase format: {"Ch01_00": "p.6-7"}
    return ", ".join(sorted(set(book_ref.values())))


def _select_nodes_by_priority(
    nodes: list[KnowledgeNode], limit: int
) -> list[KnowledgeNode]:
    """Select up to `limit` nodes, prioritizing P1 > P2 > P3."""
    priority_order = {"P1": 0, "P2": 1, "P3": 2}
    sorted_nodes = sorted(nodes, key=lambda n: priority_order.get(n.priority, 3))
    return sorted_nodes[:limit]


def _collect_outside_prereqs(
    target_node_ids: set[str],
    data_store: DataStore,
) -> list[str]:
    """Recursively collect prerequisite IDs outside the target set."""
    all_prereqs: set[str] = set()
    visited: set[str] = set()

    def _walk(node_id: str) -> None:
        if node_id in visited:
            return
        visited.add(node_id)
        node = data_store.get_node(node_id)
        if not node:
            return
        for prereq_id in node.prerequisites:
            if prereq_id not in target_node_ids:
                all_prereqs.add(prereq_id)
            _walk(prereq_id)

    for nid in target_node_ids:
        _walk(nid)

    return sorted(all_prereqs)


def select_warmup_questions(
    target_node_ids: set[str],
    data_store: DataStore,
    target_min: int = 2,
    target_max: int = 4,
    book_name: str = "",
) -> list[WarmupQuestion]:
    """Select warmup questions from prerequisite nodes outside the target set."""
    prereq_ids = _collect_outside_prereqs(target_node_ids, data_store)
    if not prereq_ids:
        return []

    # Collect candidate (node, check_point) pairs
    candidates: list[tuple[KnowledgeNode, CheckPoint]] = []
    for pid in prereq_ids:
        node = data_store.get_node(pid)
        if not node or not node.check_points:
            continue
        for cp in node.check_points:
            candidates.append((node, cp))

    if not candidates:
        return []

    # Evenly distribute across prerequisite nodes (round-robin)
    selected: list[tuple[KnowledgeNode, CheckPoint]] = []
    nodes_with_cps: list[tuple[KnowledgeNode, list[CheckPoint]]] = []
    for pid in prereq_ids:
        node = data_store.get_node(pid)
        if not node or not node.check_points:
            continue
        shuffled = list(node.check_points)
        random.shuffle(shuffled)
        nodes_with_cps.append((node, shuffled))

    if not nodes_with_cps:
        return []

    pointers = [0] * len(nodes_with_cps)
    while len(selected) < target_max:
        added = False
        for i, (node, cps) in enumerate(nodes_with_cps):
            if len(selected) >= target_max:
                break
            if pointers[i] < len(cps):
                selected.append((node, cps[pointers[i]]))
                pointers[i] += 1
                added = True
        if not added:
            break

    # Trim to at least target_min (but we always return what we have up to target_max)
    questions: list[WarmupQuestion] = []
    for idx, (node, cp) in enumerate(selected):
        q, a = parse_check_point(cp, node.understanding_goals)
        ref_pages = _get_reference_pages(node, book_name)
        book_label = f"{book_name} " if book_name else ""
        questions.append(
            WarmupQuestion(
                number=idx + 1,
                question=q,
                answer=a,
                node_id=node.id,
                node_name=node.name,
                reference_pages=ref_pages,
                note=f"この知識は今回の範囲の前提です。不安なら先に {book_label}{ref_pages} を復習しましょう。",
            )
        )

    return questions


def _assign_sentences_to_nodes(
    section_ids: list[str],
    target_nodes: list[KnowledgeNode],
    data_store: DataStore,
) -> dict[str, list[SentenceQuestion]]:
    """Assign sentences to nodes based on knowledge_tag overlap.

    Returns a dict mapping node_id -> list of SentenceQuestion (max 1 per node).
    No global cap; each node with matching sentences gets one.
    """
    target_node_ids = {n.id for n in target_nodes}

    # Collect all practice sentences from drill sections
    all_practice: list[tuple[Sentence, str, str]] = []  # (sentence, source_pages, section_id)
    for sid in section_ids:
        section = data_store.get_section(sid)
        if not section or section.type == "introduction":
            continue
        sentences = data_store.get_sentences(sid)
        for s in sentences:
            if s.role == "practice":
                all_practice.append((s, section.pages if section else "", sid))

    if not all_practice or not target_nodes:
        return {}

    # Assign each sentence to its best-matching target node
    node_assignments: dict[str, list[tuple[int, Sentence, str, str]]] = {
        n.id: [] for n in target_nodes
    }

    for sent, pages, sid in all_practice:
        sent_tags = set(sent.knowledge_tags)
        # Score against all target nodes, pick the best
        best_node_id: str | None = None
        best_score = 0
        for node in target_nodes:
            score = len(sent_tags & {node.id})
            if score > best_score:
                best_score = score
                best_node_id = node.id
        # Fallback: first target node whose ID appears in tags
        if best_node_id is None:
            for nid in sent.knowledge_tags:
                if nid in target_node_ids:
                    best_node_id = nid
                    break
        if best_node_id is not None:
            overlap = len(sent_tags & {best_node_id})
            node_assignments[best_node_id].append((overlap, sent, pages, sid))

    # For each node, randomly pick 1 sentence from its candidates
    result: dict[str, list[SentenceQuestion]] = {}
    for node in target_nodes:
        candidates = node_assignments.get(node.id, [])
        if not candidates:
            continue
        _, sent, pages, sid = random.choice(candidates)
        # Build focus_points from knowledge_tags
        focus_points: list[str] = []
        for tag in sent.knowledge_tags:
            tag_node = data_store.get_node(tag)
            if tag_node:
                focus_points.append(tag_node.name)
        sq = SentenceQuestion(
            number=0,  # renumbered later
            english=sent.english,
            japanese=sent.japanese,
            structure=sent.structure.get("全体", ""),
            notes=sent.notes,
            knowledge_tags=sent.knowledge_tags,
            focus_points=tuple(focus_points),
            source_pages=pages,
            source_section=sid,
        )
        result[node.id] = [sq]

    return result


def _build_review_guide(
    sentence_questions: list[SentenceQuestion],
    target_node_ids: set[str],
    data_store: DataStore,
    book_name: str = "",
) -> list[ReviewGuide]:
    """Build review guide from sentence knowledge_tags + prerequisites."""
    if not sentence_questions:
        return []

    all_related: set[str] = set()
    for sq in sentence_questions:
        for tag in sq.knowledge_tags:
            all_related.add(tag)
            node = data_store.get_node(tag)
            if node:
                for prereq_id in node.prerequisites:
                    all_related.add(prereq_id)

    guides: list[ReviewGuide] = []
    for nid in sorted(all_related):
        node = data_store.get_node(nid)
        if not node:
            continue
        ref_pages = _get_reference_pages(node, book_name)
        is_prereq = nid not in target_node_ids
        reason = "前提知識" if is_prereq else ""
        guides.append(
            ReviewGuide(
                node_id=nid,
                node_name=node.name,
                reference_pages=ref_pages,
                reason=reason,
            )
        )

    return guides


def build_node_sections(
    target_nodes: list[KnowledgeNode],
    sentence_map: dict[str, list[SentenceQuestion]],
    target_node_ids: set[str],
    data_store: DataStore,
    max_checks_per_node: int = 2,
    book_name: str = "",
) -> list[NodeSection]:
    """Build NodeSection list: knowledge questions + sentences + review guide per node."""
    sections: list[NodeSection] = []

    for sec_num, node in enumerate(target_nodes, start=1):
        # Knowledge questions from check_points (randomly sample up to max)
        kqs: list[KnowledgeQuestion] = []
        sampled_cps = random.sample(
            list(node.check_points),
            min(max_checks_per_node, len(node.check_points)),
        )
        for cp in sampled_cps:
            q, a = parse_check_point(cp, node.understanding_goals)
            ref_pages = _get_reference_pages(node, book_name)
            kqs.append(
                KnowledgeQuestion(
                    number=0,  # renumbered later
                    question=q,
                    answer=a,
                    node_id=node.id,
                    node_name=node.name,
                    reference_pages=ref_pages,
                )
            )

        sqs = sentence_map.get(node.id, [])
        review = _build_review_guide(sqs, target_node_ids, data_store, book_name)

        sections.append(
            NodeSection(
                section_number=sec_num,
                node_id=node.id,
                node_name=node.name,
                reference_pages=_get_reference_pages(node, book_name),
                knowledge_questions=kqs,
                sentence_questions=sqs,
                review_guide=review,
            )
        )

    return sections


def build_test_data(
    section_ids: list[str],
    data_store: DataStore,
    book_name: str = "はじめの英文読解ドリル",
) -> TestData:
    """Build complete TestData from section IDs."""
    # Collect all target knowledge nodes
    target_node_ids: set[str] = set()
    for sid in section_ids:
        section = data_store.get_section(sid)
        if section:
            target_node_ids.update(section.knowledge_nodes)

    # Load actual node objects (sorted by ID for stable output)
    nodes: list[KnowledgeNode] = []
    for nid in sorted(target_node_ids):
        node = data_store.get_node(nid)
        if node:
            nodes.append(node)

    # Warmup questions from prerequisite nodes
    warmup = select_warmup_questions(
        target_node_ids, data_store, book_name=book_name
    )

    # Assign sentences to nodes
    sentence_map = _assign_sentences_to_nodes(section_ids, nodes, data_store)

    # Build node sections
    node_sections = build_node_sections(
        nodes, sentence_map, target_node_ids, data_store, book_name=book_name
    )

    # Renumber all questions with continuous numbering
    number = 1
    for ns in node_sections:
        for i, kq in enumerate(ns.knowledge_questions):
            ns.knowledge_questions[i] = KnowledgeQuestion(
                number=number,
                question=kq.question,
                answer=kq.answer,
                node_id=kq.node_id,
                node_name=kq.node_name,
                reference_pages=kq.reference_pages,
            )
            number += 1
        for i, sq in enumerate(ns.sentence_questions):
            ns.sentence_questions[i] = SentenceQuestion(
                number=number,
                english=sq.english,
                japanese=sq.japanese,
                structure=sq.structure,
                notes=sq.notes,
                knowledge_tags=sq.knowledge_tags,
                focus_points=sq.focus_points,
                source_pages=sq.source_pages,
                source_section=sq.source_section,
            )
            number += 1

    # Build display range
    if section_ids:
        sections_label = f"{section_ids[0]}〜{section_ids[-1]}"
    else:
        sections_label = ""

    return TestData(
        sections=section_ids,
        sections_label=sections_label,
        warmup_questions=warmup,
        node_sections=node_sections,
        generated_at=datetime.now(timezone.utc).isoformat(),
        book_name=book_name,
    )
