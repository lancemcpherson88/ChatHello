from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World from Cloud Run!")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), HelloWorldHandler)
    print("Starting server on port 8080...")
    server.serve_forever()