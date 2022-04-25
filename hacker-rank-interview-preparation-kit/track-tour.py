#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # petrolpumps = [[1, 5], [10, 3], [3, 4]]
    # i = 1, j = 2 
    for i in range(len(petrolpumps)):
        b = 0
        started = True
        for j in range(len(petrolpumps)):
            aj = i+j if i+j < len(petrolpumps) else len(petrolpumps) - (i+j)
            p, d = petrolpumps[aj]
            b += p-d
            if b < 0:
                break
            if aj == i and started is not True:
                return i
            started = False
 
    return -1

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', 'test.out'), 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
