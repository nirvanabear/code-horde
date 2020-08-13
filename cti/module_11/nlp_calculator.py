
'''
You are working on a very small part of a natural language processing engine. You want your engine to be able to respond to math properly. Your colleagues have written a program that can identify when a user is asking a math question, but they haven't written a calculator!
Your job is to create a calculator that will parse natural language, and speak in natural language. To simplify the problem, you will only ever receive two operands, and all operands will be under one hundred.

Given a statement like:

"add two and seven"

return "nine".

"subtract six from four"

return "negative two"


To help with this, recognize that dictionaries can hold any value, including functions!



** pseudocode **

split string
search list for match with operator words:
    add, plus, subtract, minus, divided by, divide, multiplied by
    multiply, to the power of, root
use operator as key in dict to find the correlating function
search list for two matches to operand words:
    one, two, three... twelve... twenty two, twenty-two... one hundred
    retain order of the two operands
input operands as arguments to the function
convert return from function call into words




'''

import re

def nlp_calculator(statement):
  dashed = list_to_dict(the_hundreds)
  dashless = list_to_dict(the_hundreds, '-', ' ')
  spaceless = list_to_dict(the_hundreds, '-', '')
  all_together = {**dashed, **dashless, **spaceless}

  sentence = re.split(r'\W*\s+', statement)
  operands = []
  for index in range(len(sentence)):
    if sentence[index] in translator:
      operator = translator[sentence[index]]
    elif sentence[index] in all_together:
      if index < len(sentence) - 1 and sentence[index + 1] in all_together:
        combined = sentence[index] + " " + sentence[index + 1]
        if combined in all_together:
          operands.append(all_together[combined])
          index += 1
      else:
        operands.append(all_together[sentence[index]])
  print(operands)
  print(operator(operands[0], operands[1]))


  
  return ""
  
  
  
def add(a,b):
  return a + b


def subtract(a,b):
  return a - b


def multiply(a,b):
  return a * b


def divide(a,b):
  return a / b


def list_to_dict(array, char = '', sub = ''):
  modified = [re.sub(char, sub, element) for element in array]
  mod_dict = {modified[i]:i for i in range(101)}
  return mod_dict
  
  
translator = {
  "add": add,
  "plus": add,
  "subtract": subtract,
  "minus": subtract,
  "take away": subtract,
  "multiply": multiply,
  "times": multiply,
  "divide": divide,
  "division": divide,
  "divided": divide,
  "over": divide
}

the_hundreds = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine', 'thirty', 'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four', 'thirty-five', 'thirty-six', 'thirty-seven', 'thirty-eight', 'thirty-nine', 'forty', 'forty-one', 'forty-two', 'forty-three', 'forty-four', 'forty-five', 'forty-six', 'forty-seven', 'forty-eight', 'forty-nine', 'fifty', 'fifty-one', 'fifty-two', 'fifty-three', 'fifty-four', 'fifty-five', 'fifty-six', 'fifty-seven', 'fifty-eight', 'fifty-nine', 'sixty', 'sixty-one', 'sixty-two', 'sixty-three', 'sixty-four', 'sixty-five', 'sixty-six', 'sixty-seven', 'sixty-eight', 'sixty-nine', 'seventy', 'seventy-one', 'seventy-two', 'seventy-three', 'seventy-four', 'seventy-five', 'seventy-six', 'seventy-seven', 'seventy-eight', 'seventy-nine', 'eighty', 'eighty-one', 'eighty-two', 'eighty-three', 'eighty-four', 'eighty-five', 'eighty-six', 'eighty-seven', 'eighty-eight', 'eighty-nine', 'ninety', 'ninety-one', 'ninety-two', 'ninety-three', 'ninety-four', 'ninety-five', 'ninety-six', 'ninety-seven', 'ninety-eight', 'ninety-nine', 'one hundred']



if __name__ == "__main__":
  phrase = "subtract two and three"
  nlp_calculator(phrase)


# dashless = [re.sub('-', ' ', element) for element in the_hundreds]
# merged = [re.sub(' ', '', item) for item in dashless]

# dashed = {}
# undashed = {}
# one_word = {}
# for r in range(101):
#   dashed[the_hundreds[r]] = r
#   undashed[dashless[r]] = r
#   one_word[merged[r]] = r
