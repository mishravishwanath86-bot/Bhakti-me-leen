-- ====================================================================
-- BHAKTI APP: SCALABLE RELIGIOUS CONTENT DATABASE SCHEMA
-- Scalability: 5,000 to 50,000+ Items with SQLite 3 + FTS5
-- ====================================================================

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;

-- 1. DEITIES MASTER TABLE (19+ Gods & Goddesses)
CREATE TABLE IF NOT EXISTS deities (
    id TEXT PRIMARY KEY,                           -- e.g. 'ram', 'krishna', 'shiva'
    name_hi TEXT NOT NULL,                         -- e.g. 'श्री राम'
    name_en TEXT NOT NULL,                         -- e.g. 'Shri Ram'
    icon_emoji TEXT,                               -- e.g. '🏹'
    thumbnail TEXT,                                -- e.g. 'assets/deities/deity_ram.jpg'
    description TEXT,                              -- Brief bio / description
    display_order INTEGER NOT NULL DEFAULT 0,      -- Ordering index in UI
    is_active INTEGER NOT NULL DEFAULT 1           -- 1 = Active, 0 = Inactive
);

-- 2. CONTENT TYPES MASTER TABLE (13 Primary Types)
CREATE TABLE IF NOT EXISTS content_types (
    id TEXT PRIMARY KEY,                           -- e.g. 'bhajan', 'aarti', 'chalisa'
    name_hi TEXT NOT NULL,                         -- e.g. 'भजन'
    name_en TEXT NOT NULL,                         -- e.g. 'Bhajan'
    icon TEXT,                                     -- e.g. '🎵'
    display_order INTEGER NOT NULL DEFAULT 0,
    is_active INTEGER NOT NULL DEFAULT 1
);

-- 3. THEOLOGICAL / THEMATIC CATEGORIES TABLE
CREATE TABLE IF NOT EXISTS categories (
    id TEXT PRIMARY KEY,                           -- e.g. 'bhakti', 'gyan', 'leela', 'stuti'
    name_hi TEXT NOT NULL,                         -- e.g. 'भक्ति रस'
    name_en TEXT NOT NULL,                         -- e.g. 'Bhakti Rasa'
    description TEXT,
    display_order INTEGER NOT NULL DEFAULT 0
);

-- 4. MAIN CONTENT ITEMS TABLE (50k+ Capacity)
CREATE TABLE IF NOT EXISTS content_items (
    id TEXT PRIMARY KEY,                           -- Unique slug / UUID (e.g. 'bhajan-krishna-achyutam-keshavam')
    title TEXT NOT NULL,                           -- Hindi Title (e.g. 'अच्युतम केशवम कृष्ण दामोदरम')
    title_en TEXT,                                 -- English / Transliterated Title
    deity_id TEXT NOT NULL,                        -- FK -> deities.id
    category_id TEXT NOT NULL,                     -- FK -> categories.id
    content_type TEXT NOT NULL,                    -- FK -> content_types.id
    language TEXT NOT NULL DEFAULT 'hi',           -- 'hi', 'sa', 'en', 'hi-Latn'
    short_description TEXT,                        -- 1-2 sentence overview
    content TEXT NOT NULL,                         -- Full lyrics / shloka text / katha script
    thumbnail TEXT,                                -- Image path / URL
    audio_url TEXT,                                -- MP3 path / streaming URL
    video_url TEXT,                                -- YouTube URL / Video stream
    duration INTEGER NOT NULL DEFAULT 0,           -- Duration in seconds
    tags TEXT,                                     -- JSON Array of strings e.g. '["श्रीकृष्ण", "भजन"]'
    is_popular INTEGER NOT NULL DEFAULT 0,         -- 1 = True, 0 = False
    is_featured INTEGER NOT NULL DEFAULT 0,        -- 1 = True, 0 = False
    is_trending INTEGER NOT NULL DEFAULT 0,        -- 1 = True, 0 = False
    status TEXT NOT NULL DEFAULT 'published',      -- 'draft', 'published', 'archived'
    content_hash TEXT NOT NULL UNIQUE,             -- SHA-256 (Normalized title + deity + content_type)
    search_keywords TEXT,                          -- Pre-computed bilingual search tokens
    view_count INTEGER NOT NULL DEFAULT 0,         -- Analytics counter
    play_count INTEGER NOT NULL DEFAULT 0,         -- Audio play counter
    share_count INTEGER NOT NULL DEFAULT 0,        -- Share counter
    created_at TEXT NOT NULL,                      -- ISO-8601 UTC
    updated_at TEXT NOT NULL,                      -- ISO-8601 UTC
    FOREIGN KEY (deity_id) REFERENCES deities(id) ON UPDATE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON UPDATE CASCADE,
    FOREIGN KEY (content_type) REFERENCES content_types(id) ON UPDATE CASCADE
);

-- 5. FTS5 VIRTUAL TABLE FOR BILINGUAL FULL-TEXT SEARCH
CREATE VIRTUAL TABLE IF NOT EXISTS content_fts USING fts5(
    content_id UNINDEXED,
    title,
    title_en,
    short_description,
    content,
    search_keywords,
    tags,
    tokenize = 'unicode61 remove_diacritics 2'
);

-- 6. AUTOMATIC FTS5 SYNCHRONIZATION TRIGGERS
CREATE TRIGGER IF NOT EXISTS trg_content_ai AFTER INSERT ON content_items BEGIN
    INSERT INTO content_fts(content_id, title, title_en, short_description, content, search_keywords, tags)
    VALUES (new.id, new.title, new.title_en, new.short_description, new.content, new.search_keywords, new.tags);
END;

CREATE TRIGGER IF NOT EXISTS trg_content_au AFTER UPDATE ON content_items BEGIN
    UPDATE content_fts SET 
        title = new.title,
        title_en = new.title_en,
        short_description = new.short_description,
        content = new.content,
        search_keywords = new.search_keywords,
        tags = new.tags
    WHERE content_id = old.id;
END;

CREATE TRIGGER IF NOT EXISTS trg_content_ad AFTER DELETE ON content_items BEGIN
    DELETE FROM content_fts WHERE content_id = old.id;
END;

-- 7. PERFORMANCE INDEXES (Covering queries for < 2ms response time)
CREATE UNIQUE INDEX IF NOT EXISTS idx_content_hash ON content_items(content_hash);
CREATE INDEX IF NOT EXISTS idx_content_filter ON content_items(status, content_type, deity_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_content_popular ON content_items(status, is_popular, view_count DESC);
CREATE INDEX IF NOT EXISTS idx_content_featured ON content_items(status, is_featured, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_content_trending ON content_items(status, is_trending, play_count DESC);
CREATE INDEX IF NOT EXISTS idx_content_deity_status ON content_items(deity_id, status, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_content_type_status ON content_items(content_type, status, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_content_created_at ON content_items(status, created_at DESC, id);
