import http.server
import socketserver
import os

PORT = 5000
DIRECTORY = os.path.join(os.path.dirname(__file__), "dut_green_tracker_fixed", "build", "web")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, format, *args):
        pass

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Serving Flutter web app at http://0.0.0.0:{PORT}")
    httpd.serve_forever()
