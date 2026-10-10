import urllib.request

try:
    resp = urllib.request.urlopen("http://localhost:8000/index.html")
    print(f"HTTP Status: {resp.status}, Content Length: {len(resp.read())}")
except Exception as e:
    print("Error:", e)
