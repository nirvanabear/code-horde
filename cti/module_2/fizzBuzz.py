'''



Understand: 	Analyze the problem statement
    take an int, make a list, replace certain multiples
Match: 		    Recall problems you have seen, determine similarities
    iterating through, finding even numbers
Plan: 			Perform the steps, write them out, describe the process
    create counter
    take integer as range in for loop
    for each loop, divide i by
        5: if true, add 1 to counter
        3: if true, add 2 to counter
    if counter equals, append   1, buzz
                                2, fizz
                                3, fizzbuzz
                                0, i as string
    return list of strings
        ***
    create counter at 0
    while n - counter:
        if not n divided by 15:
            append fizzbuzz
        else if not n divided by 5:
            append buzz
        else if not n divided by 3:
            append fizz
        else:
            append "n"
        increment counter
    flip list order 

    


Implement: 	    Translate your plan to code
Review: 		Make sure your code works, handle corner cases
Evaluate: 		Determine the time and space efficiency of your solution & improvements



    Fizzbuzz is one of the most basic problems in the coding interview world. Try to write a small and elegant code for this problem.

Given a positive integer A, return an array of strings with all the integers from 1 to N. 

But for multiples of 3 the array should have “Fizz” instead of the number. 

For the multiples of 5, the array should have “Buzz” instead of the number. 

For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead of the number.

Look at the example for more details.

Example

A = 5
Return: [1 2 Fizz 4 Buzz]

'''


class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        array = []
        counter = 1
        while A - counter - 1:
            if not counter % 15:
                array.append("FizzBuzz")
            elif not counter % 5:
                array.append("Buzz")
            elif not counter % 3:
                array.append("Fizz")
            else:
                array.append(str(counter))
            counter += 1
        return array