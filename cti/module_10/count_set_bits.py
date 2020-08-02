
'''
Given an integer value in Python, return the count of "1" bits the number has, when converted as a 32-bit unsigned integer.

For example:


1:    00000000000000000000000000000001 # return 1

2:    00000000000000000000000000000010 # return 1

3:    00000000000000000000000000000011 # return 2

4:    00000000000000000000000000000100 # return 1

5:    00000000000000000000000000000101 # return 2

100 : 00000000000000000000000000100100 # return 2

500:  00000000000000000000000111110100 # return 6







'''


def count_set_bits(num):
    counter = 0
    for bit in '{:032b}'.format(num):
        if bit == '1':
            counter += 1
    return counter

