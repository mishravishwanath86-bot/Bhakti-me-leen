import os
import sys
import re
import json
import mimetypes
import urllib.parse
import urllib.request
import urllib.error
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

# Load .env configuration
ENV_CONFIG = {}
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
if os.path.exists(env_path):
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    ENV_CONFIG[k.strip()] = v.strip().strip('"').strip("'")
    except Exception as e:
        sys.stderr.write(f"Warning: Failed reading .env: {e}\n")

GOOGLE_OAUTH_CLIENT_ID = os.environ.get(
    'GOOGLE_OAUTH_CLIENT_ID',
    ENV_CONFIG.get('GOOGLE_OAUTH_CLIENT_ID', '48974341427-9jvi5car45ahmjihg9cbacu4sk4tlnct.apps.googleusercontent.com')
)
GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get(
    'GOOGLE_OAUTH_CLIENT_SECRET',
    ENV_CONFIG.get('GOOGLE_OAUTH_CLIENT_SECRET', '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')
)
GOOGLE_OAUTH_REDIRECT_URI = os.environ.get(
    'GOOGLE_OAUTH_REDIRECT_URI',
    ENV_CONFIG.get('GOOGLE_OAUTH_REDIRECT_URI', 'http://localhost:8000/auth/oauth/google/callback')
)

# Import API Router
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from api.routes import handle_api_request

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class RangeHTTPRequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Clean logging
        sys.stderr.write(f"[{self.log_date_time_string()}] {self.command} {self.path} -> {args[1]}\n")

    def _parse_query_params(self, url: str):
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query)
        # flatten single value params
        return parsed.path, {k: v[0] for k, v in params.items()}

    def _send_no_cache_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0, post-check=0, pre-check=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD')
        self.send_header('Access-Control-Allow-Headers', '*')

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

    def do_HEAD(self):
        path, params = self._parse_query_params(self.path)
        clean_path = path.lstrip('/')
        if not clean_path or clean_path == '':
            clean_path = 'index.html'
        local_path = os.path.join(APP_ROOT, clean_path.replace('/', os.sep))
        if os.path.isdir(local_path):
            local_path = os.path.join(local_path, 'index.html')
        if not os.path.exists(local_path):
            self.send_error(404, "File Not Found")
            return
        ctype, _ = mimetypes.guess_type(local_path)
        file_size = os.path.getsize(local_path)
        self.send_response(200)
        self.send_header('Content-Type', ctype or 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(file_size))
        self._send_no_cache_headers()
        self.end_headers()

    def do_GET(self):
        path, params = self._parse_query_params(self.path)

        # Handle Google OAuth Initiation
        if path == "/auth/oauth/google":
            redirect_uri = GOOGLE_OAUTH_REDIRECT_URI
            auth_params = {
                'client_id': GOOGLE_OAUTH_CLIENT_ID,
                'redirect_uri': redirect_uri,
                'response_type': 'code',
                'scope': 'openid email profile',
                'prompt': 'select_account',
                'access_type': 'online'
            }
            auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urllib.parse.urlencode(auth_params)}"
            self.send_response(302)
            self.send_header('Location', auth_url)
            self._send_no_cache_headers()
            self.end_headers()
            return

        # Handle Google OAuth Callback
        if path == "/auth/oauth/google/callback":
            code = params.get('code')
            error = params.get('error')
            if error or not code:
                err_msg = error or 'access_denied'
                self.send_response(302)
                self.send_header('Location', f"/?auth_error={urllib.parse.quote(err_msg)}")
                self.end_headers()
                return

            redirect_uri = GOOGLE_OAUTH_REDIRECT_URI

            try:
                # Exchange code for tokens
                token_data = urllib.parse.urlencode({
                    'code': code,
                    'client_id': GOOGLE_OAUTH_CLIENT_ID,
                    'client_secret': GOOGLE_OAUTH_CLIENT_SECRET,
                    'redirect_uri': redirect_uri,
                    'grant_type': 'authorization_code'
                }).encode('utf-8')
                token_req = urllib.request.Request('https://oauth2.googleapis.com/token', data=token_data, method='POST')
                token_req.add_header('Content-Type', 'application/x-www-form-urlencoded')

                with urllib.request.urlopen(token_req, timeout=10) as token_res:
                    token_json = json.loads(token_res.read().decode('utf-8'))
                    access_token = token_json.get('access_token')

                # Fetch user profile
                user_req = urllib.request.Request('https://www.googleapis.com/oauth2/v3/userinfo')
                user_req.add_header('Authorization', f"Bearer {access_token}")
                with urllib.request.urlopen(user_req, timeout=10) as user_res:
                    user_json = json.loads(user_res.read().decode('utf-8'))

                u_name = user_json.get('name', 'भक्त साधक (Google)')
                u_email = user_json.get('email', '')
                u_picture = user_json.get('picture', 'assets/gallery/bal_ganesha_little.jpg')

                success_params = urllib.parse.urlencode({
                    'google_auth_success': '1',
                    'user_name': u_name,
                    'user_email': u_email,
                    'user_avatar': u_picture
                })
                self.send_response(302)
                self.send_header('Location', f"/?{success_params}")
                self.end_headers()
            except Exception as ex:
                self.send_response(302)
                self.send_header('Location', f"/?auth_error={urllib.parse.quote(str(ex))}")
                self.end_headers()
            return

        # Handle API Routes
        if path.startswith("/api/"):
            client_ip = self.client_address[0] if hasattr(self, 'client_address') and self.client_address else "127.0.0.1"
            headers_dict = dict(self.headers) if hasattr(self, 'headers') and self.headers else {}
            status_code, ctype, res_bytes = handle_api_request("GET", path, params, None, headers=headers_dict, client_ip=client_ip)
            self.send_response(status_code)
            self.send_header('Content-Type', ctype)
            self.send_header('Content-Length', str(len(res_bytes)))
            self._send_no_cache_headers()
            self.end_headers()
            try:
                self.wfile.write(res_bytes)
            except (ConnectionResetError, BrokenPipeError):
                pass
            return

        # Serve Static Files
        clean_path = path.lstrip('/')
        if not clean_path or clean_path == '':
            clean_path = 'index.html'

        local_path = os.path.join(APP_ROOT, clean_path.replace('/', os.sep))
        if os.path.isdir(local_path):
            local_path = os.path.join(local_path, 'index.html')

        if not os.path.exists(local_path):
            self.send_error(404, "File Not Found")
            return

        ctype, _ = mimetypes.guess_type(local_path)
        if not ctype:
            if local_path.endswith('.mp3'): ctype = 'audio/mpeg'
            elif local_path.endswith('.css'): ctype = 'text/css; charset=utf-8'
            elif local_path.endswith('.js'): ctype = 'application/javascript; charset=utf-8'
            elif local_path.endswith('.json'): ctype = 'application/json; charset=utf-8'
            elif local_path.endswith('.html'): ctype = 'text/html; charset=utf-8'
            else: ctype = 'application/octet-stream'

        file_size = os.path.getsize(local_path)
        range_header = self.headers.get('Range')

        # 206 Partial Content (Audio Byte-Range Streaming)
        if range_header:
            match = re.search(r'bytes=(\d*)-(\d*)', range_header)
            if match:
                start_str, end_str = match.groups()
                start = int(start_str) if start_str else 0
                end = int(end_str) if end_str else file_size - 1
                if start >= file_size or end >= file_size or start > end:
                    self.send_response(416, "Requested Range Not Satisfiable")
                    self.send_header('Content-Range', f'bytes */{file_size}')
                    self.end_headers()
                    return

                length = end - start + 1
                self.send_response(206, "Partial Content")
                self.send_header('Content-Type', ctype)
                self.send_header('Content-Range', f'bytes {start}-{end}/{file_size}')
                self.send_header('Content-Length', str(length))
                self.send_header('Accept-Ranges', 'bytes')
                self._send_no_cache_headers()
                self.end_headers()

                with open(local_path, 'rb') as f:
                    f.seek(start)
                    sent = 0
                    chunk_size = 64 * 1024
                    while sent < length:
                        to_read = min(chunk_size, length - sent)
                        data = f.read(to_read)
                        if not data: break
                        try:
                            self.wfile.write(data)
                        except (ConnectionResetError, BrokenPipeError):
                            break
                        sent += len(data)
                return

        # Regular 200 OK Static File Delivery
        self.send_response(200)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(file_size))
        self._send_no_cache_headers()
        self.end_headers()

        with open(local_path, 'rb') as f:
            chunk_size = 64 * 1024
            while True:
                data = f.read(chunk_size)
                if not data: break
                try:
                    self.wfile.write(data)
                except (ConnectionResetError, BrokenPipeError):
                    break

    def _read_body_json(self):
        length = int(self.headers.get('Content-Length', 0))
        if length > 0:
            raw = self.rfile.read(length)
            try:
                return json.loads(raw.decode('utf-8'))
            except Exception:
                return None
        return None

    def _dispatch_mutation(self, method: str):
        path, params = self._parse_query_params(self.path)
        body = self._read_body_json()
        client_ip = self.client_address[0] if hasattr(self, 'client_address') and self.client_address else "127.0.0.1"
        headers_dict = dict(self.headers) if hasattr(self, 'headers') and self.headers else {}
        status_code, ctype, res_bytes = handle_api_request(method, path, params, body, headers=headers_dict, client_ip=client_ip)
        self.send_response(status_code)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(res_bytes)))
        self._send_no_cache_headers()
        self.end_headers()
        try:
            self.wfile.write(res_bytes)
        except (ConnectionResetError, BrokenPipeError):
            pass

    def do_POST(self):
        self._dispatch_mutation("POST")

    def do_PUT(self):
        self._dispatch_mutation("PUT")

    def do_PATCH(self):
        self._dispatch_mutation("PATCH")

    def do_DELETE(self):
        self._dispatch_mutation("DELETE")

def run(port=8000, bind='0.0.0.0'):
    server_address = (bind, port)
    httpd = ThreadingHTTPServer(server_address, RangeHTTPRequestHandler)
    print(f"🌟 Bhakti App Multi-Threaded Server active on http://localhost:{port} (Strict No-Cache Active)...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run(port=port)
