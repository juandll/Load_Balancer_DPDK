#!/usr/bin/env python3
import os
import requests
import sys
from datetime import datetime
import time

ip=200
i=1000
f=open("TimeResponse.txt", "a")

while i >0:
	os.system("ifconfig eno1 10.0.1."+str(ip)+"/24")
	t1 = time.time()
	x= requests.get('http://20.0.2.2:8080')
	t2 = time.time()
	f.write(str(t2-t1)+"\n")
	i= i-1
	ip = ip +1
	if(ip > 220):
		ip = 200
