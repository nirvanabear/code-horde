
'''

Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:
Given numRows = 5,
Return:

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]

Recursion:
Would probably use a function within a function
Would start with 5, then whittle down to 1
Would take the answer returned from a lower number to determine higher
Would take 1 as the base case

accumulator: add lists to this list
# How to make one list from the earlier:
if numRows is 1:
Append [1] to the list
return list
else

numRows = 4
prev = [1,2,1]
#     [1,3,3,1]
[1, prev[0] + prev[1], prev[1] + prev[2], 1]


numRows = 5
prev = [1,3,3,1]
#     [1,4,6,4,1]
[1, prev[0] + prev[1], prev[1] + prev[2], prev[2] + prev[3], 1]

current = [1]
for i in range(len(numRows) - 2):
     current.append(prev[i] + prev[i + 2])
current.append(1)

previous = recursive_fn(n)
accumulator.append(previous)



'''

# Question: it would appear that even after a list is appended to a
# list, the list within the list will still be modified if both are 
# taken as an argument in sequence.

def pascal_triangle(numRows):
     
     accumulator = []
     pascal_recursion(numRows, accumulator)
     print(accumulator)
     return accumulator

def pascal_recursion(numRows, accumulator):

     if numRows == 1:
          current = [1]
          accumulator.append(current)
          return current

     elif numRows == 2:
          pascal_recursion(numRows - 1, accumulator)
          current = [1,1]
          accumulator.append(current)
          return current

     else:
          prev = pascal_recursion(numRows - 1, accumulator)
          current = [1]
          for i in range(numRows - 2):
               current.append(prev[i] + prev[i + 1])
          current.append(1)
          accumulator.append(current)
          return current

pascal_triangle(8)



