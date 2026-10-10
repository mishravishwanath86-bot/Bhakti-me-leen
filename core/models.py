# ====================================================================
# BHAKTI APP: CORE CONTENT MODELS AND TYPE DEFINITIONS
# ====================================================================

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
import json

class ContentType(str, Enum):
    BHAJAN = 'bhajan'
    AARTI = 'aarti'
    CHALISA = 'chalisa'
    MANTRA = 'mantra'
    STOTRAM = 'stotram'
    KATHA = 'katha'
    DHARMIK_GYAN = 'dharmik_gyan'
    SATSANG = 'satsang'
    CHETAWANI_BHAJAN = 'chetawani_bhajan'
    FESTIVAL_SPECIAL = 'festival_special'
    VRAT_KATHA = 'vrat_katha'
    TEMPLE_KATHA = 'temple_katha'
    NAAM_JAAP = 'naam_jaap'

class Deity(str, Enum):
    RAM = 'ram'
    KRISHNA = 'krishna'
    RADHARANI = 'radharani'
    SHIVA = 'shiva'
    HANUMAN = 'hanuman'
    DURGA_MATA = 'durga_mata'
    GANESH = 'ganesh'
    VISHNU = 'vishnu'
    LAKSHMI = 'lakshmi'
    SARASWATI = 'saraswati'
    SURYA = 'surya'
    SHANIDEV = 'shanidev'
    KHATUSHYAM = 'khatushyam'
    BHAIRAV = 'bhairav'
    SANTOSHI = 'santoshi'
    GANGA = 'ganga'
    YAMUNA = 'yamuna'
    GURU_SANT = 'guru_sant'
    OTHER_DEITIES = 'other_deities'
    GENERAL_BHAKTI = 'general_bhakti'

class ContentStatus(str, Enum):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    ARCHIVED = 'archived'

class Language(str, Enum):
    HINDI = 'hi'
    SANSKRIT = 'sa'
    ENGLISH = 'en'
    HINGLISH = 'hi-Latn'

@dataclass
class ContentItem:
    id: str
    title: str
    deity_id: str
    category_id: str
    content_type: str
    content: str
    title_en: Optional[str] = None
    language: str = 'hi'
    short_description: Optional[str] = None
    thumbnail: Optional[str] = None
    audio_url: Optional[str] = None
    video_url: Optional[str] = None
    duration: int = 0
    tags: List[str] = field(default_factory=list)
    is_popular: bool = False
    is_featured: bool = False
    is_trending: bool = False
    status: str = 'published'
    content_hash: Optional[str] = None
    search_keywords: Optional[str] = None
    view_count: int = 0
    play_count: int = 0
    share_count: int = 0
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def __post_init__(self):
        now_iso = datetime.now(timezone.utc).isoformat()
        if not self.created_at:
            self.created_at = now_iso
        if not self.updated_at:
            self.updated_at = now_iso
        if isinstance(self.tags, str):
            try:
                self.tags = json.loads(self.tags)
            except Exception:
                self.tags = [t.strip() for t in self.tags.split(',') if t.strip()]

    def to_db_row(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'title': self.title,
            'title_en': self.title_en or '',
            'deity_id': self.deity_id,
            'category_id': self.category_id,
            'content_type': self.content_type,
            'language': self.language,
            'short_description': self.short_description or '',
            'content': self.content,
            'thumbnail': self.thumbnail or '',
            'audio_url': self.audio_url or '',
            'video_url': self.video_url or '',
            'duration': int(self.duration or 0),
            'tags': json.dumps(self.tags, ensure_ascii=False) if isinstance(self.tags, list) else '[]',
            'is_popular': 1 if self.is_popular else 0,
            'is_featured': 1 if self.is_featured else 0,
            'is_trending': 1 if self.is_trending else 0,
            'status': self.status,
            'content_hash': self.content_hash or '',
            'search_keywords': self.search_keywords or '',
            'view_count': self.view_count,
            'play_count': self.play_count,
            'share_count': self.share_count,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    @classmethod
    def from_db_row(cls, row: Dict[str, Any]) -> 'ContentItem':
        tags_raw = row.get('tags', '[]')
        tags = []
        if isinstance(tags_raw, str):
            try:
                tags = json.loads(tags_raw)
            except Exception:
                tags = [t.strip() for t in tags_raw.split(',') if t.strip()]
        elif isinstance(tags_raw, list):
            tags = tags_raw

        return cls(
            id=row['id'],
            title=row['title'],
            title_en=row.get('title_en'),
            deity_id=row['deity_id'],
            category_id=row.get('category_id', 'bhakti'),
            content_type=row['content_type'],
            language=row.get('language', 'hi'),
            short_description=row.get('short_description'),
            content=row['content'],
            thumbnail=row.get('thumbnail'),
            audio_url=row.get('audio_url'),
            video_url=row.get('video_url'),
            duration=row.get('duration', 0),
            tags=tags,
            is_popular=bool(row.get('is_popular', 0)),
            is_featured=bool(row.get('is_featured', 0)),
            is_trending=bool(row.get('is_trending', 0)),
            status=row.get('status', 'published'),
            content_hash=row.get('content_hash'),
            search_keywords=row.get('search_keywords'),
            view_count=row.get('view_count', 0),
            play_count=row.get('play_count', 0),
            share_count=row.get('share_count', 0),
            created_at=row.get('created_at'),
            updated_at=row.get('updated_at')
        )
