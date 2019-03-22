#!/usr/bin/python
import sys

dic = {}
for line in sys.stdin:
    key, value = line.strip("\n").split("\t")
    dic.setdefault(key, 0)
    dic[key] += int(value)

sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for k, v in sorted_dic:
    print("%s\t%s" % (k,v))