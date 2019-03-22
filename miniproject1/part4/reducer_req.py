#!/usr/bin/env python3
import sys

dic = {}
for line in sys.stdin:
    key, value = line.strip("\n").split("\t")
    dic.setdefault(key, 0)
    dic[key] += int(value)

print("/assets/img/home-logo.png\t%s" % dic['/assets/img/home-logo.png'])