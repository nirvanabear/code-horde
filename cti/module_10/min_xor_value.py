
'''
Given a list of unsigned integers, find the pair of integers in the array which have the minimum XOR value. Return the minimum XOR value.

 
Examples : 
Input 
0 2 5 7 
Output 
2 (0 XOR 2) 
Input 
0 4 7 9 
Output 
3 (4 XOR 7)
Constraints: 
2 <= N <= 100 000 
0 <= A[i] <= 1 000 000 000




** repl.it unit test **

test1 = [0, 2, 3, 5, 8, 8, 9, 23, 37]

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 17, in test_more_examples
    self.assertEquals(min_xor_value([0, 2, 3, 5, 8, 8, 9, 23, 37]),0)
AssertionError: 1 != 0


'''


def min_xor_value(num):
    lowest = float('inf')
    for i in range(len(num)):
        for j in range(len(num)):
            if i != j:
                xor = num[i] ^ num[j]
                if xor < lowest:
                    lowest = xor
    return lowest
