

'''
 You are given an integer array arr of size n . Assume a sliding window of size k starting from index 0 . In each iteration, the sliding window moves to the right by one position till n-k . Write a program to return an array representing the maximum number in all sliding windows.

Problem Note

    The first element of the resultant array is max(arr[0...k]) , then the second element is max(arr[1...k+1]) and so on.
    The size of the resultant array will be n-k+1 .
    You are expected to solve this question in O(n) time complexity

Example 1

Input: arr[] = [4, 3, 8, 9, 0, 1], k = 3
Output: [8, 9, 9, 9]
Explanation: The window size is 3 and the maximum at different iterations are as follows:
max(4, 3, 8) = 8
max(3, 8, 9) = 9
max(8, 9, 0) = 9
max(9, 0, 1) = 9
Hence, we get arr = [8, 9, 9, 9] as output.

Example 2

Input: arr[] = [9, 8, 6, 4, 3, 1], k = 4
Output: [9, 8, 6]
Explanation: The window size is 4 and the maximum at different iterations are as follows:
max(9, 8, 6, 4) = 9
max(8, 6, 4, 3) = 8
max(6, 4, 3, 1) = 6
Hence, we get arr = [9, 8, 6] as output.

Example 3

Input: arr[] = [1, 2, 3, 4, 10, 6, 9, 8, 7, 5], k = 3
Output: [3, 4, 10, 10, 10, 9, 9, 8]
Explanation: The window size is 3 and the maximum at different iterations are as follows:
max(1, 2, 3) = 3
max(2, 3, 4) = 4
max(3, 4, 10) = 10
max(4, 10, 6) = 10
max(10, 6, 9) = 10
max(6, 9, 8) = 9
max(9, 8, 7) = 9
max(8, 7, 5) = 8
Hence, we get arr = [3, 4, 10, 10, 10, 9, 9, 8] as output.


****************

create 0:2 window
create maximum
for each in array:
    append to window
    pop window
    if len(window) equals 3:
        append max to maximums


'''


def slide_window_max(array, window):
    '''Return an array of max elements, one for each window of
    constant width as it slides along an array.'''
    maximum = []
    for i in range(window-1, len(array)):
        maximum.append(max(array[i-(window-1):i+1]))
    return maximum

# O(n) == n

if __name__ == "__main__":
    arr1 = [4, 3, 8, 9, 0, 1]
    k1 = 3
    arr2 = [9, 8, 6, 4, 3, 1] 
    k2 = 4
    arr3 = [1, 2, 3, 4, 10, 6, 9, 8, 7, 5] 
    k3 = 3

    print(slide_window_max(arr1, k1))
    print(slide_window_max(arr2, k2))
    print(slide_window_max(arr3, k3))