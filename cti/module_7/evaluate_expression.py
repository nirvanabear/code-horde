
'''
Reverse polish notation is a postfix notation for mathematical expressions. For example, the infix expression (1 + 2) / 3 would become 1 2 + 3 /. More detailed explanation here:  https://en.wikipedia.org/wiki/Reverse_Polish_notation

Task:
Given a mathematical expression in reverse polish notation, represented by an array of strings, find the answer to this expression. Operators consist only of +, -, *, /, and all numbers are integer values. When performing a division on two numbers, use python's integer division operator (//). Your output should be a single integer, which is the value of the expression when evaluated. Each expression is guaranteed to be valid.

Example 1:

expression = ["3", "4", "+", "5", "-"]

print(evaluate_expression(expression))

>> 2


Example 2:

expression = ["3", "4", "/", "5", "*"]

print(evaluate_expression(expression))

>> 0


Explanation 1:
"3 4 + 5 -" is equivalent to the infix expression "3 + 4 - 5"
The answer to this expression is 2.

Explanation 2:
"3 4 / 5 *" is equivalent to the infix expression "3 / 4 * 5"
Since we are using integer division, 3 / 4 = 0, and 0 * 5 = 0.
The answer to this expression is 0.





** scratch paper **

numbers = []
op_dict = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y, "/": (lambda x,y: x//y))}

# while len(numbers) < 2:
for element in list:
    if element.isnumeric():
        numbers.append(int(element))
    else:
        


[a,b] = 1,2
operator = "+"
ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y)}
# ops['+'] (1,2)
# ops['+'] [1,2]
ops[operator] (a,b)



** pseudocode **

operands = []
for element in list:
    if a number:
        append it to a operands list
    elif an operator:
        take the two numbers in the list and operate
        remove the two numbers
        append the solution to the operands list
return operands[0]


'''

def evaluate_expression(expression):
    operands = []
    op_dict = {"+": (lambda x,y: x+y), 
               "-": (lambda x,y: x-y), 
               "*": (lambda x,y: x*y), 
               "/": (lambda x,y: x//y)}
    # while len(numbers) < 2:
    for element in expression:
        if element.isnumeric():
            operands.append(int(element))
        else:
            b = operands.pop()
            a = operands.pop()
            # a,b = operands
            solution = op_dict[element](a,b)
            # operands.clear()
            operands.append(solution)
    return operands[0]


expression1 = ["3", "4", "+", "5", "-"]
expression2 = ["3", "4", "/", "5", "*"]

print(evaluate_expression(expression1))

