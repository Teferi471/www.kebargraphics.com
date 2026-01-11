#!/usr/bin/env python3
import http.server
import socketserver
import os

# Change to the directory containing your website
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

Handler = MyHTTPRequestHandler

print("Starting server...")
print(f"Your website will be available at:")
print(f"http://localhost:{PORT}")
print(f"http://127.0.0.1:{PORT}")
print("\nTo access from phone on same WiFi:")
print("1. Find your computer's IP address")
print("2. Use http://YOUR-IP-ADDRESS:8000")
print("\nPress Ctrl+C to stop the server")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")