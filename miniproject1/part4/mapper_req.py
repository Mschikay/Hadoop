#!/usr/bin/python
import sys
import re

for line in sys.stdin:
    quest = re.findall(r'"(.*?)"', line)[0]
    if not quest:
        continue
    method, url, protocol = quest.split()
    if method != "GET":
        continue
    print("{0}\t{1}".format(url, 1))