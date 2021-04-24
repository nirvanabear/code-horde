'''


Problem: Given an input string in the form of a+b or a-b, evaluate the expression and return the resule.

Constraints:
# 1) a and b will be single digit.
# 2) only one operation '+' or '-'
# 3) there will be no space in the string

Example input/output
# 1) 5+8 -> 13
# 2) 8-5 -> 3
# 3) 5-8 -> -3


** pseudocode **
loop through string with indeces:
    if not a number:
        store string[:index] as an int in a
        store string[index + 1:] as an int in b
        if current char is +:
            solution is a + b
        else:
            solution is a - b




'''

def simpleCalculator(expression):
   for m in range(len(expression)):
      if not expression[m].isnumeric():
         a = int(expression[:m])
         b = int(expression[m+1:])
         if expression[m] == "+":
            solution = a + b
         else:
            solution = a - b
   return solution





