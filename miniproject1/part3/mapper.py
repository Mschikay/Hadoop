#!/usr/bin/python
import sys

def ngram(n, text):
    n = int(n)
    text_list = list(text)
    res = []
    for i in range(len(text_list)-n+1):
        res.append(''.join(text_list[i:i+n]))
    return res

if len(sys.argv) > 1:
    n = sys.argv[1]
else:
    n = '1'


for line in sys.stdin:
    string = line.strip('\n')
    ngram_list = ngram(n, string)
    for x in ngram_list:
        print("{0}\t{1}".format(x, 1))
