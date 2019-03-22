#!/usr/bin/python
import sys
import re

for line in sys.stdin:
    ip_address = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)[0]
    
    print("{0}\t{1}".format(ip_address, 1))