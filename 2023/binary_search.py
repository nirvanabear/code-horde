'''
Binary Search Algorithm – Iterative and Recursive Implementation
Google Translate Icon

Given a sorted array of n integers and a target value, determine if the target exists in the array in logarithmic time using the binary search algorithm. If target exists in the array, print the index of it.

(Divide array in half, then recursively or iteratively search for item)

For example,
Input:
 
nums[] = [2, 3, 5, 7, 9]
target = 7
 
Output: Element found at index 3
 
 
Input:
 
nums[] = [1, 4, 5, 8, 9]
target = 2
 
Output: Element not found 
'''

# Odd, even length? datatype? 
# Edge case: length of 1 or 0
    # divide by // gives 0 for len=1
        # checking that index ends algo
        # if no match, return "None"
    # len=2: gives 1
        # checking index
        # if greater than, end algo, no match
        # else divide by 2
    # len=3: gives 1
        # checking index
        # len=1 either way
    # 0: if len < 1, return "No array"

def binary_search(array, target, start, end):
    '''Search by dividing array in half, taking half which
    includes target and search again until matched.'''
    # Divide length of array by half:  L // 2
    # Check index
        # if match, return fn
        # else:
            # if <: send lower half as arg to fn
            # if >: send upper as arg to fn

    index = ((end - start) // 2) + start
    print(index, start, end)

    if (end - start) == 1 and array[index] != target:
        return None
    elif array[index] == target:
        return index
    elif target < array[index]:
        end = index
        return binary_search(array, target, start, end)
    elif target > array[index]:
        start = index
        return binary_search(array, target, start, end)

# O(n) == log n

if __name__ == "__main__":
    array1 = [2, 3, 5, 7, 9, 10, 15, 18, 22, 27, 30, 32]
    array2 = [1, 4, 5, 8, 9]
    target1 = 7
    target2 = 4
    print(binary_search(array1, target1, 0, 12))
    print(binary_search(array2, target2, 0, 5))