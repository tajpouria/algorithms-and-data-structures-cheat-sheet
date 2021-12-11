#! /usr/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "1.in"

inp = [int(i) for i in open(infile).read().strip().split("\n")]

p = 0
inc = 0
for i, el in enumerate(inp):
    if i > 0 and el > p:
        inc += 1
       
    p = el

print(inc)

