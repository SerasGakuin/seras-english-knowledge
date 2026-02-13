-- ============================================================
-- cross_book_links: 参考書間のノードリンク
-- Phase F: 複数参考書の独立ネットワーク接続
-- ============================================================
-- 手動で Supabase SQL Editor にて実行すること

CREATE TABLE cross_book_links (
  id          SERIAL PRIMARY KEY,
  source_node TEXT NOT NULL REFERENCES knowledge_nodes(id) ON DELETE CASCADE,
  target_node TEXT NOT NULL REFERENCES knowledge_nodes(id) ON DELETE CASCADE,
  link_type   TEXT NOT NULL,  -- 'same_concept' / 'extends' / 'prerequisite'
  notes       TEXT,
  UNIQUE (source_node, target_node)
);

CREATE INDEX idx_cbl_source ON cross_book_links(source_node);
CREATE INDEX idx_cbl_target ON cross_book_links(target_node);
