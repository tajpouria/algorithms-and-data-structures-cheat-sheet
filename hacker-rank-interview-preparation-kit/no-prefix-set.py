#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#


def noPrefix(words):
    ht_prefix = {}
    ht_word = {}
    for w in words:
        check = ""
        if w in ht_prefix:
            print("BAD SET")
            print(w)
            return
        for l in w:
            check += l
            ht_prefix[check] = 1
            if check in ht_word:
                print("BAD SET")
                print(w)
                return
        ht_word[w] = 1
    print("GOOD SET")


if __name__ == "__main__":
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
