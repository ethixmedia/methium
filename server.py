"""Methium local server. Serves the player at http://127.0.0.1:5173 (the address Spotify sends you back to)."""
import http.server, os, sys, threading, webbrowser

HOST, PORT = "127.0.0.1", 5173
ROOT = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def do_GET(self):
        if self.path.split("?")[0] in ("/", "/callback", "/callback/"):
            self.path = "/index.html"
        return super().do_GET()
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()
    def log_message(self, *a):
        pass

try:
    server = http.server.ThreadingHTTPServer((HOST, PORT), Handler)
except OSError:
    print(f"Port {PORT} is already in use. Methium may already be running: open http://{HOST}:{PORT}")
    webbrowser.open(f"http://{HOST}:{PORT}")
    sys.exit(0)

url = f"http://{HOST}:{PORT}"
print(f"Methium is running at {url}\nKeep this window open while you listen. Press Ctrl+C to stop.")
threading.Timer(0.6, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nMethium stopped.")
