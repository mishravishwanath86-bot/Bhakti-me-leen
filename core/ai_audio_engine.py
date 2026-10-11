# ====================================================================
# BHAKTI APP: AI BHAKTI SINGING & DEVOTIONAL AUDIO ENGINE
# 100% Free Mode Powered by Edge-TTS Neural Speech + Devotional Cadence
# ====================================================================

import os
import re
import sys
import hashlib
import asyncio
from typing import Dict, Any, Optional

# Base directory for cached audio
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AI_AUDIO_DIR = os.path.join(BASE_DIR, "assets", "ai_audio")
os.makedirs(AI_AUDIO_DIR, exist_ok=True)

# Voice Configurations
VOICE_MAP = {
    "male": "hi-IN-MadhurNeural",       # Resonant, Pandit/Rishi Devotional Voice
    "female": "hi-IN-SwaraNeural",     # Melodious, Devkanya/Meera Devotional Voice
    "default": "hi-IN-MadhurNeural"
}

# Devotional Cadence Tuning per Content Type
CADENCE_SETTINGS = {
    "mantra": {"rate": "-10%", "pitch": "+0Hz"},
    "stotram": {"rate": "-8%", "pitch": "+0Hz"},
    "gita": {"rate": "-8%", "pitch": "+1Hz"},
    "shloka": {"rate": "-8%", "pitch": "+1Hz"},
    "chalisa": {"rate": "-4%", "pitch": "+2Hz"},
    "aarti": {"rate": "-3%", "pitch": "+2Hz"},
    "bhajan": {"rate": "-2%", "pitch": "+3Hz"},
    "katha": {"rate": "-2%", "pitch": "+0Hz"},
    "satsang": {"rate": "-2%", "pitch": "+0Hz"},
    "vrat_katha": {"rate": "-2%", "pitch": "+0Hz"},
    "temple_katha": {"rate": "-2%", "pitch": "+0Hz"},
    "default": {"rate": "-4%", "pitch": "+1Hz"}
}

def clean_devotional_text(raw_text: str) -> str:
    """
    Cleans raw text, strips HTML tags, English annotations, and format brackets
    while strictly preserving Sanskrit visargas, viramas, anuswaras, and danda stops.
    """
    if not raw_text:
        return ""

    # 1. Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', raw_text)

    # 2. Remove bracketed markers like [दोहा], [चौपाई], (1), [Verse]
    text = re.sub(r'\[[^\]]*\]', '', text)
    text = re.sub(r'\([^\)]*(?:chorus|verse|meaning|भावार्थ)[^\)]*\)', '', text, flags=re.IGNORECASE)

    # 3. Remove English lyrics/translations if mixed in
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        # If line is only English ASCII characters (like website credits or roman script), skip
        ascii_chars = sum(1 for c in line if ord(c) < 128 and c.isalpha())
        devanagari_chars = sum(1 for c in line if 0x0900 <= ord(c) <= 0x097F)
        if ascii_chars > 15 and devanagari_chars == 0:
            continue
        # Replace multiple spaces
        line = re.sub(r'\s+', ' ', line)
        lines.append(line)

    cleaned = "\n".join(lines)
    return cleaned.strip()

def compute_cache_key(content_id: str, text: str, voice_key: str, content_type: str) -> str:
    """Generates unique deterministic filename hash."""
    seed = f"{content_id}_{voice_key}_{content_type}_{text[:200]}_{len(text)}"
    return hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12]

async def _synthesize_edge_tts(text: str, voice: str, rate: str, pitch: str, output_path: str):
    """Generates MP3 using edge_tts async communicate."""
    import edge_tts
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(output_path)

def generate_ai_bhakti_audio(
    content_id: str,
    text: str,
    title: str = "",
    content_type: str = "aarti",
    voice: str = "male",
    custom_speed: float = 1.0
) -> Dict[str, Any]:
    """
    On-Demand Audio Generator:
    Checks permanent disk cache first. If absent, generates neural audio and caches it.
    """
    cleaned_text = clean_devotional_text(text)
    if not cleaned_text:
        return {
            "success": False,
            "error": "सामग्री का टेक्स्ट रिक्त है (Text is empty)"
        }

    voice_id = VOICE_MAP.get(voice.lower(), VOICE_MAP["default"])
    c_type = (content_type or "default").lower()
    cadence = CADENCE_SETTINGS.get(c_type, CADENCE_SETTINGS["default"])

    # Adjust rate if user specified custom speed
    rate_str = cadence["rate"]
    if custom_speed != 1.0:
        pct = int((custom_speed - 1.0) * 100)
        sign = "+" if pct >= 0 else ""
        rate_str = f"{sign}{pct}%"

    pitch_str = cadence["pitch"]

    cache_hash = compute_cache_key(str(content_id), cleaned_text, voice.lower(), c_type)
    file_name = f"bhakti_{content_id}_{voice.lower()}_{cache_hash}.mp3"
    full_path = os.path.join(AI_AUDIO_DIR, file_name)
    web_url = f"/assets/ai_audio/{file_name}"

    # 1. Check if already cached on disk
    if os.path.exists(full_path) and os.path.getsize(full_path) > 2048:
        return {
            "success": True,
            "cached": True,
            "audio_url": web_url,
            "title": title,
            "voice": voice,
            "content_type": content_type,
            "size_bytes": os.path.getsize(full_path)
        }

    # 2. Fresh generation via Edge-TTS (Free Mode)
    try:
        # If text is very long (e.g. 50+ lines of katha), process cleanly
        asyncio.run(_synthesize_edge_tts(cleaned_text, voice_id, rate_str, pitch_str, full_path))

        if os.path.exists(full_path) and os.path.getsize(full_path) > 1024:
            return {
                "success": True,
                "cached": False,
                "audio_url": web_url,
                "title": title,
                "voice": voice,
                "content_type": content_type,
                "size_bytes": os.path.getsize(full_path)
            }
        else:
            return {
                "success": False,
                "error": "ऑडियो फ़ाइल उत्पन्न नहीं हो सकी (File size 0)"
            }
    except Exception as e:
        sys.stderr.write(f"[AIAudioEngine] Synthesis error: {e}\n")
        return {
            "success": False,
            "error": f"ऑडियो सृजन में त्रुटि: {str(e)}"
        }
