
'''
Sort a list of integers, using only "pancake flips". A pancake flip is defined as taking the first k elements of a list and reversing them. Your function should return a list of integers, containing the k-values for each flip. So long as the series of flips you return creates a sorted list, the answer is correct.

Example:
destination = len(nums)

[5, 2, 3, 4, 1]; Starting array
# Move largest to end
search range(5)
index = 0
destination = 5
swap(nums, 5)

[1, 4, 3, 2, 5]; Reverse first 5 integers, k=5
# Move next largest to beginning
search range(4)
index = 1
destination = 4
swap(nums, 2)   # index + 1

[4, 1, 3, 2, 5]; Reverse first 2 integers, k=2
# Move next largest to the end
no search
index = 0
destination = 4
swap(nums, 4)
destination -= 1

[2, 3, 1, 4, 5]; Reverse first 4 integers, k=4
# Move next next largest to beginning
search range(3)
index = 1
destination = 3
swap(nums, 2)

[3, 2, 1, 4, 5]; Reverse first 2 integers, k=2
# Move next next largest to the end
no search
index = 0
destination = 3
swap(nums, 3)
destination -= 1

[1, 2, 3, 4, 5]; Reverse first 3 integers, k=3

Sorted!
k-values are: [5, 2, 4, 2, 3]



** pseudocode **
# list_slice = nums

largest = float('-inf')
largest_index = 0
destination = len(nums)

while destination > 1:
    for m in range(destination):
        if nums[m] > largest:
            largest = nums[m]
            largest_index = m

    if largest_index != 0:
        swap(nums, largest_index + 1)

    if largest_index = 0:
        swap(nums, destination)
        destination -= 1
        






'''


def flip(arr, k):
    for i in range(k//2):
        arr[i], arr[k-i-1] = arr[k-i-1], arr[i]

def pancake_sort(nums):
    # largest = float('-inf')
    largest_index = 0
    destination = len(nums)
    nums_sorted = sorted(nums)
    k_values = []

    # print(nums)

    while destination > 1:
        # print('destination: ' + str(destination))
        largest = float('-inf')
        for m in range(destination):
            if nums[m] > largest:
                largest = nums[m]
                largest_index = m
                
        # print('largest: ' + str(largest))        
        # print('index: ' + str(largest_index))

        if largest_index != 0:
            flip(nums, largest_index + 1)
            k_values.append(largest_index + 1)
            # print(nums)

        if largest_index == 0:
            flip(nums, destination)
            k_values.append(destination)
            # print(nums)
            destination -= 1

        if nums == nums_sorted:
            destination = 0
    
    # return nums
    return k_values

nums1 = [5, 2, 4, 2, 3]
nums2 = [5, 2, 3, 4, 1]
# flip(nums1, 5)
# print(nums1)
print(pancake_sort(nums2))
