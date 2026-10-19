#!/usr/bin/env python3
"""
🎮 Game Jams Panel Public Slide Deck Server (Port 3026)
Clean public production viewer for GeekGirlCon 2026 presentation deck.
Multi-threaded, Winsock-isolated, single-source browser launch.
"""

import os
import sys
import time
import socketserver
import http.server

# Force UTF-8 on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
    except Exception:
        pass

PORT = 3026
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class ProductionHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

class ThreadedProductionServer(socketserver.ThreadingTCPServer):
    daemon_threads = True
    allow_reuse_address = False

def run_server(auto_open=True):
    import webbrowser
    import threading

    if "--no-browser" in sys.argv or "--no-open" in sys.argv:
        auto_open = False

    os.chdir(ROOT_DIR)
    try:
        httpd = ThreadedProductionServer(("", PORT), ProductionHandler)
    except OSError as e:
        if "10048" in str(e) or getattr(e, "winerror", None) == 10048 or getattr(e, "errno", None) == 48:
            print("========================================================")
            print(f"⚠️  Port {PORT} is ALREADY IN USE by an active slide server.")
            if auto_open:
                print(f"🌐 Opening http://127.0.0.1:{PORT}/ in your browser...")
                webbrowser.open(f"http://127.0.0.1:{PORT}/")
            print("========================================================")
            return
        raise e

    print(f"🎮 Game Jams Public Slide Deck running at http://localhost:{PORT}")
    print(f"📁 Serving: {ROOT_DIR}")

    if auto_open:
        def _open():
            time.sleep(0.3)
            webbrowser.open(f"http://127.0.0.1:{PORT}/")
        threading.Thread(target=_open, daemon=True).start()

    with httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    run_server()
