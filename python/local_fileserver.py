#!/usr/bin/env python3

import http.server
import socketserver
import socket
import platform

platform_system = platform.system()

hostname = socket.gethostname()
if 'Linux' == platform_system: 
    from subprocess import call
    print("host ips: ")
    call(["hostname", "-I"])
else:
    my_ip=socket.gethostbyname(hostname)
    print("host ips: {0}".format(my_ip))


PORT = 8888
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at http://{0}:{1}/".format(hostname,PORT))
httpd.serve_forever()
