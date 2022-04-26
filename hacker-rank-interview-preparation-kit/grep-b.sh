# https://www.hackerrank.com/challenges/text-processing-in-linux-the-grep-command-5/problem

grep "\([0-9]\) *\1"
# [1-9]: Find a number and remember it.
# <space>*: Zero or more space in can happened.
# \1: Look for recurrence of the same number.

