import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Length of index.html:", len(html))
print("glass-youtube-container in html:", "glass-youtube-container" in html)

pos = html.find('classic-artwork-wrapper')
print("classic-artwork-wrapper position:", pos)
if pos != -1:
    print("Around classic-artwork-wrapper:\n", html[pos-100:pos+500])
