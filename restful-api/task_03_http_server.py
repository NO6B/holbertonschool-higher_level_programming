from http.server import BaseHTTPRequestHandler, HTTPServer

import json


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data)

        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            json_info = json.dumps(info).encode('utf-8')
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_info)

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_error(404, "Endpoint not found")


def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serveur lancé sur http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
