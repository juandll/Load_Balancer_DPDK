#!/usr/bin/env python3
import os
import psutil
import socket
import time
UDP_IP = "20.0.2.99"
UDP_PORT = 5700
opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while 1:
	time.sleep(3)
	cpu_pr = psutil.cpu_percent(0.1)
	cpu_pr_int=int(cpu_pr)
	MESSAGE = cpu_pr_int.to_bytes(2,'little')
	print(cpu_pr_int)
	os.system('arp -s 20.0.2.99 02:00:00:00:00:01')
	opened_socket.sendto(MESSAGE, (UDP_IP, UDP_PORT))
