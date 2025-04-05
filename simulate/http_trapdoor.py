from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
TRAPDOOR_PATH = "/supersecret"

class TrapdoorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/login":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Login page: please authenticate.")
        elif self.path == TRAPDOOR_PATH:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Welcome, admin. Trapdoor access granted!")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found.")

    def log_message(self, format, *args):
        # Suppress noisy logs for demo purposes
        return

def run_server():
    server_address = ("0.0.0.0", 8080)
    httpd = HTTPServer(server_address, TrapdoorHandler)
    print("🚪 Trapdoor server running on http://localhost:8080")
    print("🕳️  Secret admin backdoor: http://localhost:8080/supersecret")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()