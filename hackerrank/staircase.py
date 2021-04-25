#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/staircase/

# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#
'''
** pseudocode **
for p in range(n):
    print n - p spaces and print p octothorpes
'''

def staircase(n):
    # Write your code here
    for p in range(1, n + 1):
        print((" " * (n - p)) + ("#" * p))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
