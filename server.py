from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

os.chdir(r'X:\LUCHA')
PORT = 8000

with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()