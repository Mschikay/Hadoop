#!/usr/bin/python
import sys

dic = {}
for line in sys.stdin:
    key, value = line.strip("\n").split()
    dic.setdefault(key, 0)
    dic[key] += int(value)

try: 
    for k, v in dic.items():
        print("%s\t%s".format(k, v))
except BrokenPipeError as e:
    pass  # Ignore. Something like head is truncating output.
finally:
    sys.stderr.close()
