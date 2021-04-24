#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''
** pseudocode **
create positive counter
create negative counter
create zero counter
for each element in the array:
    if the element is larger than 0:
        increment positive
        ...
'''

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    for each in arr:
        if each > 0:
            positive += 1
        elif each < 0:
            negative += 1
        else:
            zero += 1
    print(f"{positive/len(arr):.6f}\n{negative/len(arr):.6f}\n{zero/len(arr):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
