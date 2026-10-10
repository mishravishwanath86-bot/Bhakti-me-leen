import subprocess
import time
import json
import urllib.request
import base64

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
proc = subprocess.Popen([
    edge_path,
    "--headless=new",
    "--remote-debugging-port=9222",
    "--window-size=412,860",
    "http://localhost:8000/index.html"
])

try:
    time.sleep(3)
    # Get debug target
    targets = json.loads(urllib.request.urlopen("http://localhost:9222/json").read())
    print("Targets found:", len(targets))
    ws_url = targets[0]["webSocketDebuggerUrl"]
    print("WebSocket URL:", ws_url)
finally:
    proc.terminate()
