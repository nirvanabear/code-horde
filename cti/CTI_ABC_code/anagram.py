

'''
Problem

Given two strings, str_a and str_b, determine if str_b is a substring of str_a.

Constraints

   str_b will always be smaller or the same size as str_a
   the comparison is case sensitive.

Examples

   avocadotoast, avocado -> True
   avocadotoast, avocadotoast -> True
   hotcakes, cake -> True
   frenchtoast, Toast -> False
   frenchtoast, fret -> False

Explanations

   str_b is smaller than str_a and str_b is found in str_a.
   str_b is the same size as str_a and str_b is found in str_a.
   str_b b is smaller than str_a and str_b is found in str_a.
   str_b is not found in str_a because of the case difference.
   str_b is not found in str_a.




** pseudocode **


loop with indeces through str_a
   check if slice[i:]
      if the letter matches, then keep checking
      else, go to next letter in str_a
'''


x, y =  "avocadotoast", "Toastavocado"


def isAnagramSimple(str_a,str_b):
   if(len(str_b) > len(str_a)):
      return False
   else:
      i = 0
      isAnagram = False
      while i + len(str_b) <= len(str_a) and not isAnagram:
         if set(list(str_a[i: i+len(str_b)].lower())) == set(list(str_b.lower())):
            isAnagram = True
         else:
            i += 1
      return isAnagram
     

print(isAnagramSimple(x,y))
