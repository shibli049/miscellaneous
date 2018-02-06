#!/usr/bin/env python3
import http.server
import socketserver
import socket
my_ip=socket.gethostbyname(socket.gethostname())
PORT = 8888
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at http://{0}:{1}/".format(my_ip,PORT))
httpd.serve_forever()
