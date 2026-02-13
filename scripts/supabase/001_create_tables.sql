-- ============================================================
-- seras-knowledge DDL
-- Phase E-1: YAML -> Supabase (PostgreSQL) migration
-- ============================================================

-- ============================================================
-- 1. knowledge_nodes
-- ============================================================
CREATE TABLE knowledge_nodes (
  id          TEXT PRIMARY KEY,
  name        TEXT NOT NULL,
  category    TEXT NOT NULL,
  priority    TEXT NOT NULL DEFAULT 'P3',
  notes       TEXT
);

-- ============================================================
-- 2. knowledge_node_prerequisites (self M:N)
-- ============================================================
CREATE TABLE knowledge_node_prerequisites (
  node_id         TEXT NOT NULL REFERENCES knowledge_nodes(id) ON DELETE CASCADE,
  prerequisite_id TEXT NOT NULL REFERENCES knowledge_nodes(id) ON DELETE CASCADE,
  PRIMARY KEY (node_id, prerequisite_id),
  CHECK (node_id != prerequisite_id)
);

-- ============================================================
-- 3. understanding_goals (1:N ordered)
-- ============================================================
CREATE TABLE understanding_goals (
  id      SERIAL PRIMARY KEY,
  node_id TEXT NOT NULL REFERENCES knowledge_nodes(id) ON DELETE CASCADE,
  seq     INT  NOT NULL,
  goal    TEXT NOT NULL
);
CREATE UNIQUE INDEX uq_goals_node_seq ON understanding_goals(node_id, seq);

-- ============================================================
-- 4. check_points (1:N ordered)
-- ============================================================
CREATE TABLE check_points (
  id       SERIAL PRIMARY KEY,
  node_id  TEXT NOT NULL REFERENCES knowledge_nodes(id) ON DELETE CASCADE,
  seq      INT  NOT NULL,
  question TEXT NOT NULL,
  answer   TEXT NOT NULL DEFAULT ''
);
CREATE UNIQUE INDEX uq_checks_node_seq ON check_points(node_id, seq);

-- ============================================================
-- 5. knowledge_references (1:N per book)
-- ============================================================
CREATE TABLE knowledge_references (
  id         SERIAL PRIMARY KEY,
  node_id    TEXT NOT NULL REFERENCES knowledge_nodes(id) ON DELETE CASCADE,
  book       TEXT NOT NULL,
  section_id TEXT,
  pages      TEXT
);
CREATE UNIQUE INDEX uq_refs_node_book ON knowledge_references(node_id, book);

-- ============================================================
-- 6. sections
-- ============================================================
CREATE TABLE sections (
  id    TEXT PRIMARY KEY,
  book  TEXT NOT NULL,
  title TEXT NOT NULL,
  pages TEXT NOT NULL,
  type  TEXT NOT NULL DEFAULT 'drill'
);

-- ============================================================
-- 7. section_knowledge_nodes (M:N ordered)
-- ============================================================
CREATE TABLE section_knowledge_nodes (
  section_id TEXT NOT NULL REFERENCES sections(id) ON DELETE CASCADE,
  node_id    TEXT NOT NULL REFERENCES knowledge_nodes(id) ON DELETE CASCADE,
  seq        INT  NOT NULL,
  PRIMARY KEY (section_id, node_id)
);

-- ============================================================
-- 8. section_prerequisites (self M:N)
-- ============================================================
CREATE TABLE section_prerequisites (
  section_id      TEXT NOT NULL REFERENCES sections(id) ON DELETE CASCADE,
  prerequisite_id TEXT NOT NULL REFERENCES sections(id) ON DELETE CASCADE,
  PRIMARY KEY (section_id, prerequisite_id),
  CHECK (section_id != prerequisite_id)
);

-- ============================================================
-- 9. sentences
-- ============================================================
CREATE TABLE sentences (
  id         TEXT PRIMARY KEY,
  section_id TEXT NOT NULL REFERENCES sections(id) ON DELETE CASCADE,
  drill      INT  NOT NULL,
  number     INT  NOT NULL,
  role       TEXT NOT NULL DEFAULT 'practice',
  english    TEXT NOT NULL,
  japanese   TEXT NOT NULL,
  notes      TEXT
);
CREATE INDEX idx_sentences_section ON sentences(section_id);

-- ============================================================
-- 10. sentence_structures (1:N)
-- ============================================================
CREATE TABLE sentence_structures (
  id          SERIAL PRIMARY KEY,
  sentence_id TEXT NOT NULL REFERENCES sentences(id) ON DELETE CASCADE,
  label       TEXT NOT NULL,
  value       TEXT NOT NULL
);
CREATE UNIQUE INDEX uq_struct_sent_label ON sentence_structures(sentence_id, label);

-- ============================================================
-- 11. sentence_knowledge_tags (M:N)
-- ============================================================
CREATE TABLE sentence_knowledge_tags (
  sentence_id TEXT NOT NULL REFERENCES sentences(id) ON DELETE CASCADE,
  node_id     TEXT NOT NULL REFERENCES knowledge_nodes(id) ON DELETE CASCADE,
  PRIMARY KEY (sentence_id, node_id)
);
CREATE INDEX idx_tags_node ON sentence_knowledge_tags(node_id);
