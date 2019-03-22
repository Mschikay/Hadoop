#!/usr/bin/python
import sys

count = 0
for line in sys.stdin:
    key, value = line.strip("\n").split("\t")
    if key == '"/assets/img/home-logo.png”':
        value += 1

print("The hits are: ", value)