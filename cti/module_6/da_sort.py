
'''
You recently learned a new way to sort an array of numbers in your algorithms course. The algorithm sorts an array of numbers by repeatedly performing the Delete-and-Append operation. The Delete-and-Append operation consists of three steps:

    Choose an element from the array.
    Delete the chosen element from the array.
    Append the chosen element to the end of the array.

Being a curious student, you wonder what is the minimum number of Delete-and-Append operations required to sort a given array.

Instructions:
Given an array of integers, find out the minimum number of Delete-Append operations that are required to make the array sorted. 

You can solve this problem in a number of ways. 
Hint 1: Could you somehow find out how many operations are necessary by looking at the already sorted version of the array?
Hint 2: Alternatively, it is possible to find out the minimum number of required operations without sorting the list?

Example:
[1, 5, 2, 4, 3, 6]; Starting array
[1, 5, 2, 3, 6, 4]; DA 4
[1, 2, 3, 6, 4, 5]; DA 5
[1, 2, 3, 4, 5, 6]; DA 6

Done! Took three operations.

Original site: https://open.kattis.com/problems/dasort 



** pseudocode **
swapCount = 0
r = 0
s = 0
while r < len(sorted_array) and s < len(unsorted):
    if sortDone[r] == unsorted[s]:
        r += 1
        s += 1
    elif sortDone[r] != unsorted[s]:
        swapCount += 1
        s += 1
return swapCount

'''

# input: an array of integers
# output: an integer, how many da operations are needed to sort this array
def da_sort(nums):
    sortDone = merge_sort(nums)
    # print(sortDone)
    unsorted = nums
    swapCount = 0
    r = 0
    s = 0
    while r < len(sortDone) and s < len(unsorted):
        if sortDone[r] == unsorted[s]:
            # print(sortDone[r])
            # print(unsorted[s])
            r += 1
            s += 1
        elif sortDone[r] != unsorted[s]:
            # print(sortDone[r])
            # print(unsorted[s])
            swapCount += 1
            s += 1
    # print("swapCount: " + str(swapCount))
    return swapCount


# recursive version:
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    else:
        # divide array into halves
        pivot = len(nums) // 2
        half1 = nums[:pivot]
        half2 = nums[pivot:] 
        # print("push: " + str(half1) + ", " + str(half2))
        half1 = merge_sort(half1)
        half2 = merge_sort(half2)
        # print("pop: " + str(half1) + ", " + str(half2))
        temp_array = merge(half1, half2)
        return temp_array


def merge(half1, half2):
    i = 0
    j = 0
    temp_array = []
    # Start here: 
    # Never mind that you don't know where halves come from
    while i < len(half1) and j < len(half2):
        if half1[i] <= half2[j]:
            # add half1[i] to temp_array
            temp_array.append(half1[i])
            # i++
            i += 1
        else:
            # add half2[j] to temp_array
            temp_array.append(half2[j])
            # j++
            j += 1
    # add rest of array where i or j is less than len to temp_array
    if i == len(half1):
        temp_array.extend(half2[j:])
    else:
        temp_array.extend(half1[i:])
    return temp_array

array = [1, 5, 2, 4, 3, 6]
print(da_sort(array))
# print(merge_sort(array))

