#!/usr/bin/env python3
import sys

dic = {}
for line in sys.stdin:
    key, value = line.strip("\n").split("\t")
    dic.setdefault(key, 0)
    dic[key] += int(value)

print("10.153.239.5\t%s" % dic['10.153.239.5'])