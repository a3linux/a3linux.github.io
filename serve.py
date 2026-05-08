#!/usr/bin/env python3
import http.server
import socketserver
import socket
import threading

PORT = 9090

handler = http.server.SimpleHTTPRequestHandler

class IPv6Server(socketserver.TCPServer):
    address_family = socket.AF_INET6
    allow_reuse_address = True

ipv4 = socketserver.TCPServer(("127.0.0.1", PORT), handler)
ipv6 = IPv6Server(("::1", PORT), handler)

print(f"Serving at http://127.0.0.1:{PORT}")
print(f"Serving at http://localhost:{PORT}")

t = threading.Thread(target=ipv6.serve_forever, daemon=True)
t.start()

ipv4.serve_forever()
