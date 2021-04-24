'''
Given a list of distinct integers from 0 to a value MAX_VALUE, write a function to produce a string that describes the ranges of numbers missing from the list.
The items in the result should be sorted in ascending order and separated by commas. When a gap spans only one number, the item is the number itself; when a gap is longer, the item comprises the start and the end of the gap, joined with a minus sign.

Example:

MAX_VALUE = 1000
VALUES = [0, 1, 2, 50, 52, 75]
RESULT = "3-49,51,53-74,76-1000"



** pseudocode **

create empty output string ""
if first value in list not equal to 0:
   if second value in list not equal to 1:
      append string "0-" + "second value - 1" + ","
   else:
      append string "1,"
loop with an index over almost each value in VALUES:
   (loop will start at i = 1, not 0)
   if value not equal to previous value + 1 and previous value + 1 not equal to current - 1:
      append string "previous value + 1" + "-" + "current value - 1" + "," to output string
   elif value not equal to previous value + 1:
      append string "previous value + 1" + "," to output
if last value not equal to MAX_VALUE:
   if second to last value not equal to MAX_VALUE - 1:
      append string "second to last + 1" + "-" + "MAX_VALUE"
   else:
      append string "MAX_VALUE"




'''

def missingElementStepI(arr):
   max_value = len(arr);
   for index in range(max_value):
      # print(index)
      if index > 0:
         if arr[index-1] != arr[index] - 1:
            output = arr[index] - 1
            return output
   if index == max_value - 1:
      output = max_value
      return output


missingElementStepI([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


def missingElementStepII(arr, max_value):
   return_value = "";
   if arr[0] != 0:
      numList = [i for i in range(arr[0])]
      return_value = ", ".join(map(str, numList)) + ", "
   for j in range(1,len(arr)):
      if arr[j] != arr[j-1] + 1:
         numList = [i for i in range(arr[j-1] + 1, arr[j])]
         return_value = return_value + ", ".join(map(str, numList)) 
   if arr[-1] != max_value:
      numList = [i for i in range(arr[-1] + 1, max_value + 1)]
      return_value = return_value + ", ".join(map(str, numList))
   return return_value




def missingElementStepIII(arr, max_value):
   return_value = "";
   if arr[0] != 0:
      if arr[0] != 1:
         return_value = "0-" + str(arr[0] - 1) + ", "
      else:
         return_value = "0,"
   for j in range(1,len(arr)):
      if arr[j] != arr[j-1] + 1:
         if arr[j-1] + 1 != arr[j] - 1:
            return_value = return_value + str(arr[j-1] + 1) + "-" + str(arr[j] - 1) + ", "
         else:
            return_value = return_value  + str(arr[j-1] + 1) + ", "
   if arr[-1] != max_value:
      if arr[-1] != max_value - 1:
         return_value = return_value + str(arr[-1] + 1) + "-" + str(max_value)
      else:
         return_value = return_value + str(max_value)
   if return_value[-1] == ",":
      return_value = return_value[:-1]
   return return_value

   
