import http.server
import socketserver
import socket

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        headers = self.headers
        source_ip, source_port = self.request.getsockname()  # Get the local (server) IP and port

        response  = f"Client IP Address : {client_ip}\n"
        response += f"Server IP Address : {source_ip}\n"
        response += f"\nHTTP Request Headers:\n{headers}\n"
        response += f"\n============================="
        response += f"\n\n    This is US-East Server"
        response += f"\n\n=============================\n"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        client_ip = self.client_address[0]
        headers = self.headers
        source_ip, source_port = self.request.getsockname()  # Get the local (server) IP and port

        response  = f"Client IP Address : {client_ip}\n"
        response += f"Server IP Address : {source_ip}\n"
        response += f"\nHTTP Request Headers:\n{headers}\n"
        response += f"\nPOST Data:\n{post_data}\n"
        response += f"\n============================="
        response += f"\n\n    This is US-East Server"
        response += f"\n\n=============================\n"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode())

PORT = 80

with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
