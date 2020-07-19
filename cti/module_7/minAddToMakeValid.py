

'''
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

    It is the empty string, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.


Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Input

    S.length <= 1000
    S only consists of '(' and ')' characters.


Sample Output
input#1

())

output#1

1


input#2

(((

output#2

3


input#3

()

output#3

0



input#4

()))((

output#4

4


** pseudocode **

if parenthesis is left, push onto stack
if parenthesis is right, and len(stack) > 0, pop off parenthesis
else push onto stack
return len(stack)




'''


def minAddToMakeValid(S):
    # stack = []
    left = 0
    right = 0
    for paren in S:
        if paren == '(':
            # stack.append(paren)
            left += 1
        elif paren == ')' and left > 0:
            left -= 1
        else:
            right += 1
    return left + right


paren1 = '())'

paren2 = '((('

paren3 = '()'

paren4 = '()))(('

print(minAddToMakeValid(paren4))