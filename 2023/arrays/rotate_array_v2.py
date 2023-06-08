'''
Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.

Examples:  

    Input: 
    arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
    Output: 3 4 5 6 7 1 2

    Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
    Output: 5 6 7 1 2 3 4
'''

'''
get remainder from integer % size
take slice from 0 to remainder
concat with slice from remainder to end
if negative, 
get remainder
concat negative slices from remainder to end
'''

def rotate_array(arr, move):
    remain = move % len(arr)
    new_arr = arr[remain:] + arr[:remain]
    return new_arr


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    move1 = 2
    print(rotate_array(arr1, move1))
    arr2 = [3, 4, 5, 6, 7, 1, 2]
    move2 = -2
    print(rotate_array(arr2, move2))
