#!/usr/bin/env python3
import os
import requests
import sys
import socketserver
import http.server
from datetime import datetime
import psutil

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
	daemon_threads = True

port = 8080
server = ThreadedHTTPServer(('20.0.2.2',port), http.server.SimpleHTTPRequestHandler)
try:
	server.serve_forever()
except KeyboardInterrupt:
	pass

