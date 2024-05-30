#!/usr/bin/python3
"""
This module contain a class SimpleHTTPRequestHandler to set up a web server
"""


import http.server
import socketserver
import json

PORT = 8000


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Simple HTTP request handler with GET endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests.

        - Responds with a greeting message at the root endpoint.
        - Serves JSON data at the /data endpoint.
        - Provides an OK status at the /status endpoint.
        - Returns a 404 Not Found for undefined endpoints.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            self.send_response(200)  # HTTP status 200 OK
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
