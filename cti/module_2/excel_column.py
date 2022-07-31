'''

Understand: 	Analyze the problem statement
    string to int

Match: 		Recall problems you have seen, determine similarities
    creating a base 26 to decimal converter
    similar to base 2 or base 16 to decimal

Plan: 			Perform the steps, write them out, describe the process
    no zeros
    Z       26
    AA      26 + 1
    AZ      26 + 26 
    BA      (26 * 2) + 1
    BZ      (26 * 2) + 26
    CA      (26 * 3) + 1
    ZZ      (26 * 26) + 26
    AAA     (26 * 26) + 26 + 1
    AAZ     (26 * 26) + 26 + 26
    ABA     (26 * 26) + (26 * 2) + 1
    AZZ     (26 * 26) + (26 * 26) + 26
    BAA     (26 * 26 * 2) + (26 * 1) + 1
 
    reverse
    iterate through:
        A-Z -> 26^0 * (1 through 26)
        A-Z -> 26^1 * (1 through 26)
        A-Z -> 26^2 * (1 through 26)
            either increment a variable, or iterate with i in range
        
    
Implement: 	Translate your plan to code
Review: 		Make sure your code works, handle corner cases
Evaluate: 		Determine time & space efficiency of solution


Problem Description
 
 

Given a column title A as appears in an Excel sheet, return its corresponding column number.


Problem Constraints

1 <= |A| <= 100


Input Format

First and only argument is string A.


Output Format

Return an integer


Example Input

Input 1:

 "A"

Input 2:

 "AB"



Example Output

Output 1:

 1

Output 2:

 28



Example Explanation

Explanation 1:

 A -> 1

Explanation 2:

A  -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
'''



class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        power = 0
        total = 0
        for letter in reversed(A):
            total += (26 ** power) * (ord(letter) - 64)
            power += 1
        return total

if __name__ == "__main__":
    mary = Solution()
    print(mary.titleToNumber("A"))
    print(mary.titleToNumber("Z"))
    print(mary.titleToNumber("AA"))
    print(mary.titleToNumber("AZ"))
    print(mary.titleToNumber("ZZ"))
    print(mary.titleToNumber("AAA"))