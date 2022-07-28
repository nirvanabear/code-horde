
'''


Understand: 	Analyze the problem statement
Match: 		Recall problems you have seen, determine similarities
    iterators, comparisons
Plan: 			Perform the steps, write them out, describe the process
    iterate and multiply through range of A
    iterate through string version of the number, compare to 0
        ***

Logarithmic solution:
    Understanding: Comparisons count for O(n) complexity
    Match: binary search- cuts n in half each time
    Plan: 
        Count the number of times 5 divides into n??!?!?

Implement: 	Translate your plan to code
Review: 		Make sure your code works, handle corner cases
Evaluate: 		Determine the time and space efficiency of your solution & improvements


Problem Description
 
 

Given an integer A, return the number of trailing zeroes in A!.

Note: Your solution should be in logarithmic time complexity.



Problem Constraints

0 <= A <= 10000000


Input Format

First and only argumment is integer A.


Output Format

Return an integer, the answer to the problem.


Example Input

Input 1:

 A = 4

Input 2:

 A = 5



Example Output

Output 1:

 0

Output 2:

 1



Example Explanation

Explanation 1:

 4! = 24

Explanation 2:

 5! = 120
'''



class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        counter = 0
        while A >= 5:
            counter += (A // 5)
            A /= 5
        return counter        




# Brute force solution:

# def trailZ(B):
#     count2 = 0
#     for each in range(1,B):
#         B *= each
#     for every in reversed(str(B)):
#         if every == "0":
#             count2 += 1
#         else:
#             break
#     return count2
     