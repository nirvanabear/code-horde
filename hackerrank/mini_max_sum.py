#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/mini-max-sum/

# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''
** pseudocode **
create sum accumulator array
create target variable
create min_max array
for each of the min_max array:
    create target_found boolean and set to False
    find min of the array
    set target equal to min
    for each in array:
        if not equal to target and target_found is True:
            add each to sum 
        elif each equal to target:
            set target_found to True
print 

** pseudocode v2**
create sum accumulator array
create min_max array
for each of the min_max array:
    copy parameter array
    create target_found boolean and set to False
    find each() as a function, with array as the argument
    remove min or max from array copy
    sum the new array
    append sum to sum accumulator array
print string of sum_array[0] + " " + sum_array[1]

'''


def miniMaxSum(arr):
    # Write your code here
    sum_array = []
    min_max = [max, min]
    for each in min_max:
        array_copy = arr.copy()
        extreme = each(array_copy)
        array_copy.remove(extreme)
        sum_array.append(sum(array_copy))
    print(str(sum_array[0]) + " " + str(sum_array[1]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
