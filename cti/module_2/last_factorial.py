'''

Understand: 	Analyze the problem statement
    N is 10 at max, so that's pretty narrow

Match: 		Recall problems you have seen, determine similarities
    write out array of input and output and look for mathematical link
    similar to calculus problems

Plan: 			Perform the steps, write them out, describe the process
    after looking at the output table, I don't much see the point
    result will end in 0 once 5 (and 2) are involved
    otherwise, it's just:
    1   1
    2   2
    3   6
    4   4

Implement: 	Translate your plan to code
Review: 		Make sure your code works, handle corner cases
Evaluate: 		Determine time & space efficiency of solution

Last Factorial Digit
/problems/lastfactorialdigit/file/statement/en/img-0001.jpg
Factorials on the complex plane, by Dmitrii Kouznetsov

The factorial of N, written as N!, is defined as the product of all the integers from 1 to N. For example, 3!=1×2×3=6.

This number can be very large, so instead of computing the entire product, just compute the last digit of N! (when N! is written in base 10).

Input

The first line of input contains a positive integer 1≤T≤10, the number of test cases. Each of the next T lines contains a single positive integer N. N is at most 10.

Output

For each value of NN, print the last digit of N!.

.
Sample Input 1 	
3
1
2
3

	
Sample Output 1

1
2
6

Sample Input 2 	
2
5
2

	
Sample Output 2

0
2
'''

def fact_last_dig(number):
    '''Returns the last digit of the factorial of the input.'''
    if number < 5:
        if number == 3:
            result = 6
        else:
            result = number
    else:
        result = 0
    return result



if __name__ == "__main__":

    from math import factorial

    samantha = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    for each in samantha:
        print(str(each) + ":\t" + str(factorial(each)))
        print("last digit: " + str(fact_last_dig(each)))
    
    

