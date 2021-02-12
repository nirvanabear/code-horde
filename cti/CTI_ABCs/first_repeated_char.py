'''
Problem

Identify if each character in a string is repeated in the string. If the character appears, add a ’T’ to the resulting string.

Constraints 

        Assume only alphanumeric characters are used.
        Using no additional memory aside from the output string.
        Not case sensitive.
        Using O(N^2) time.

Examples

#“CTICTI” -> "TTTTTT"
#“ABCSCTI2020” -> "TTTTTT"
#“ABCCC” -> "TTT"
#"ABCS” -> ""

Explanation

T = A character DOES appears more than once in the given string.
The number of T's represents the number of indices that contained a repeated character.*

*This was worded funny in the video...


** pseudocode **
create output string equalling ""
loop through string with p:
   loop through string with q:
      if p = q:
         append a T to output
         break
return output

OR:
   create match equals False
   create index counter equaling 0:
   while match is false and counter <= length of string:
      if p equals string[index]:
         set match equals True
         append to output string a T
      else:
         increment index counter
return output string



'''

def firstRepeatedChar1(str):
   output = ""
   for p in range(len(str)):
      for q in range(len(str)):
         if str[p] == str[q] and q != p:
            output = output + "T"
            break
   return output


'''
#“AAAAA” -> 1
#“ABCSCTI2020” -> 3
#“ABCCC” -> 1
#"ABCS” -> 0


** pseudocode **

create empty counter dictionary
loop with index p through string:
   loop with index q through sliced string[index + 1:]:
      if string[p] equals string[q] and q not equal to p and not in dict
         add character to counter dict
count entries in counter dict
return count
but NO imports!!

SO:
create blacklist string
create counter
loop with index p through string:
   loop with index q through sliced string[index + 1:]:
      if string[p] == string[q] and q != p and not in blacklist:
         increment counter
         break


'''

def firstRepeatedCharII(str):
   blacklist = ""
   counter = 0
   for r in range(len(str)):
      for s in range(r, len(str)):
         if str[r] == str[s] and r != s and str[r] not in blacklist:
            blacklist = blacklist + str[r]
            counter += 1
            break
   return counter



'''
Constraints

    Not case sensitive.
    Assume only alphanumeric characters are given.
    You may use additional memory aside from the output string.
    More efficient than O(N^2) time

Examples

“AAAAA” -> a
“ABCSCTI2020” -> c
“ABCCC” -> c
"ABCS” -> 


'''


def firstRepeatedChar(str):
   # blacklist = ""
   # counter = 0
   repeated = ""
   for r in range(len(str)):
      for s in range(r+1, len(str)):
         if str[r] == str[s] and r != s:
            # blacklist = blacklist + str[r]
            # counter += 1
            repeated = str[r].lower()
            # break
            return repeated
   return repeated