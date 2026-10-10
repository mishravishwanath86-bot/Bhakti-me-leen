import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("--- Checking all loadYouTubePlayer calls in app.js ---")
yt_calls = re.findall(r'(\w*loadYouTubePlayer\([^)]*\))', js)
for c in yt_calls:
    print("  Call:", c)

print("\n--- Checking all container IDs referenced for YouTube in app.js ---")
containers = re.findall(r"['\"]([a-zA-Z0-9_-]*youtube[a-zA-Z0-9_-]*)['\"]", js, re.I)
for c in set(containers):
    in_html = c in html
    print(f"  Container '{c}' referenced in app.js -> Present in index.html: {in_html}")

print("\n--- Checking coreAudioElement in app.js ---")
audio_init = re.findall(r'(window\.coreAudioElement[\s\S]*?;)', js)
for ai in audio_init[:3]:
    print(" ", ai)

print("\n--- Checking audio volume / muted handling in app.js ---")
vol_muted = re.findall(r'(\.volume\s*=\s*[^;\n]+|\.muted\s*=\s*[^;\n]+)', js)
for vm in vol_muted[:10]:
    print(" ", vm)
