#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import threading
import time
import sys

PORT = 8000
HTML_FILE = "chapter01_week1_slides.html"

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppress server logs to keep terminal output clean
        pass

def start_server(port):
    handler = Handler
    while port < 9000:
        try:
            with socketserver.TCPServer(("", port), handler) as httpd:
                print(f"[SUCCESS] Local server started at http://localhost:{port}/")
                print(f"[INFO] Serving files from the slides directory.")
                print(f"[INFO] Press Ctrl+C to stop the server.")
                
                # Open browser after a brief delay to ensure server is ready
                url = f"http://localhost:{port}/{HTML_FILE}"
                threading.Thread(target=lambda: (time.sleep(0.5), webbrowser.open(url))).start()
                
                httpd.serve_forever()
        except OSError:
            # Port is busy, try the next one
            port += 1
    print("[ERROR] Could not find any open port between 8000 and 9000.")
    sys.exit(1)

if __name__ == "__main__":
    try:
        start_server(PORT)
    except KeyboardInterrupt:
        print("\n[INFO] Server stopped.")
        sys.exit(0)
