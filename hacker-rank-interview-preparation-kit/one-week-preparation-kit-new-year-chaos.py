#!/bin/python3

from distutils.log import debug
import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    q = [e-1 for e in q] # adjust to 0-index for simplicity
    bribes = 0
    for i in range(len(q)-1):
        if q[i] - i > 2:
            print("Too chaotic")
            return
        j = i
        while j >= 0 and q[j+1] < q[j]:
            q[j+1], q[j] = q[j], q[j+1]
            bribes += 1
            j -= 1
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
