
'''
Given five input numbers, a, b, c, d and n, print out the number of 1 bits at the nth least significant bit position in all four numbers a, b, c, d.

Example input I

1 1 1 1 0

Example output

4

All numbers a, b, c and d are 1 - binary equivalent of which is 0001. Since n is 0 in the input, nth lsb position is the last bit position. In all four numbers, the last bit position is 1, counting them results in 4.

Example input II

2 3 5 6 1

Example output

3

Binary equivalent of a = 0010
                                  b = 0011
                                  c = 0101
                                  d = 0110.
Since n is given as 1, it the last but one bit in each of these numbers, that bit is 1 in a, 1 in b, 0 in c and 1 in d. Counting the 1's gives us a result of 3.

Notes
Read and understand Python bitwise operators here: https://wiki.python.org/moin/BitwiseOperators - in particular << and &

This problem will help you as a stepping stone problem to solve the Single Number II problem in the IPS curriculum.






'''


number = 7




# Read two integers a & b:
input_value = input()
values = input_value.split();
a = int(values[0])
b = int(values[1])
c = int(values[2])
d = int(values[3])
n = int(values[4])

# Count the number of 1's in the nth lsb position
# in a, b, c and d and print it



