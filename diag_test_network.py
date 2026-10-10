import urllib.request, urllib.error, json, sys, os

sys.stdout.reconfigure(encoding='utf-8')

test_samples = {
    'Old Known-Good (Local MP3)': {
        'type': 'LOCAL_MP3',
        'url': 'assets/audio/bhajan_achyutam_keshavam.mp3',
        'is_local': True
    },
    'Old Known-Good (Remote/Local)': {
        'type': 'LOCAL_MP3',
        'url': 'assets/audio/katha_ramayana.mp3',
        'is_local': True
    },
    'Phase 2N Sample': {
        'type': 'YOUTUBE',
        'url': 'https://www.youtube.com/watch?v=2MWF-UHsC64',
        'is_local': False
    },
    'Phase 2O Sample': {
        'type': 'YOUTUBE',
        'url': 'https://www.youtube.com/watch?v=im-9cVVmND0',
        'is_local': False
    },
    'Phase 2P Sample': {
        'type': 'YOUTUBE',
        'url': 'https://www.youtube.com/watch?v=fQse0WNm0hE',
        'is_local': False
    },
    'Phase 2Q Sample': {
        'type': 'YOUTUBE',
        'url': 'https://www.youtube.com/watch?v=d_kH0Wb4D0w',
        'is_local': False
    }
}

results = {}

for name, info in test_samples.items():
    print(f"\nTesting {name} ({info['url']})...")
    if info['is_local']:
        # Check local file existence and size
        if os.path.exists(info['url']):
            size = os.path.getsize(info['url'])
            print(f"  ✓ Local file exists: {size} bytes")
            results[name] = {'status': 'PASS', 'http_code': 200, 'size': size, 'mode': 'HTML5_AUDIO'}
        else:
            print(f"  ✗ Local file missing")
            results[name] = {'status': 'FAIL', 'error': 'File not found', 'mode': 'HTML5_AUDIO'}
    else:
        # Check YouTube oEmbed / watch URL HTTP response
        yt_id = info['url'].split('v=')[-1]
        embed_url = f"https://www.youtube-nocookie.com/embed/{yt_id}"
        oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={yt_id}&format=json"
        try:
            req = urllib.request.Request(
                oembed_url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                print(f"  ✓ YouTube oEmbed OK: {data.get('title')[:40]}... (Author: {data.get('author_name')})")
                results[name] = {
                    'status': 'MEDIA_AVAILABLE',
                    'http_code': resp.status,
                    'title': data.get('title'),
                    'embed_url': embed_url,
                    'mode': 'YOUTUBE_EMBED'
                }
        except Exception as e:
            print(f"  ⚠️ HTTP check notice: {e}")
            results[name] = {'status': 'HTTP_NOTICE', 'error': str(e), 'mode': 'YOUTUBE_EMBED'}

print("\n--- Summary of Network Availability ---")
for k, v in results.items():
    print(f"  {k}: {v.get('status')} (Mode: {v.get('mode')})")
