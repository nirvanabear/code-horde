'''
Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.

Examples:  

    Input: 
    arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
    Output: 3 4 5 6 7 1 2

    Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
    Output: 5 6 7 1 2 3 4
'''

# length, datatype, negative numbers, length 0?
# what about rotating longer than the array length
# what about d equal to array length

def rotate_array(array, d):
    '''Rotate the array elements to the left by d positions.'''
    # Take the remainder of d / len(array)
    # Positive d:
    # Take a slice from the beginning, append it to the end
    # Remove the same slice from the beginning
    # Negative d:
    # Do the opposite.

    moves = d % len(array)
    if d < 0:
        array = array[d:] + array[0:d]
    else:
        array = array[d:] + array[0:d]
    return array


if __name__ == "__main__":
    array1 = [1, 2, 3, 4, 5, 6, 7]
    print(rotate_array(array1, -2))