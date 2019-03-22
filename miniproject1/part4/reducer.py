#!/usr/bin/python
import sys

dic = {}
for line in sys.stdin:
    key, value = line.strip("\n").split("\t")
    dic.setdefault(key, 0)
    dic[key] += int(value)

for k, v in dic.items():
    print("{0}\t{1}".format(k, v))