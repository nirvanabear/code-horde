
'''
 Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Original Site:  https://www.interviewbit.com/problems/generate-all-parentheses/ 




'''


def valid(s):
   stack = []
   paren_dic = {')':'(', '}':'{' , ']':'['}
   for paren in s:
      if paren in ['(', '[', '{']:
         stack.append(paren)
      elif paren in [')', ']', '}']:
         if stack and paren_dic[paren] == stack[-1]:
            stack.pop()
         else: 
            return 0
   if len(stack) == 0:
      return 1
   else:
      return 0
         



