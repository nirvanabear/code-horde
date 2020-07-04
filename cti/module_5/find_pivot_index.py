'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array will not contain duplicates.

Note: If you know the number of times the array is rotated, then this problem becomes trivial. If the number of rotation is x, then minimum element is A[x].

Hints on the original problem: https://www.interviewbit.com/problems/rotated-array/

  # List is sorted, but then rotated.
  # Find the minimum element in less than linear time
  # return it's index



** pseudocode **
for each in list:
    if each > each + 1:
        return index

'''


def find_pivot_index(input_list):
    for r in range(len(input_list) - 1):
        if input_list[r] > input_list[r + 1]:
            return r + 1
    return 0
