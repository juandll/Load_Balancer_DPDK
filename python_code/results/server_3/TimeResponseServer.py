#!/usr/bin/env python3
import os
import requests
import sys
from datetime import datetime
import psutil

ip=21
i=300
f=open("TimeResponse.txt", "a")

while i >0:
	cpu_pr = psutil.cpu_percent(0.1)
	cpu_pr_int = int(cpu_pr)
	f.write(str(cpu_pr_int)+"\n")
	i= i-1

