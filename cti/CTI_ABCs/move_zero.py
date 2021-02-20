'''
Stepping Stone #1

Move the zeros to the back of the array using extra space.

 

Example

    arr = [0,1,0,3,12] —> [1,3,12,0,0]



'''

def move(nums):
    new_nums = []
        new_index = 0
    for each in nums:
        if each == 0:
            new_nums.append(0)
        else:
            new_nums.insert(new_index, each)
            new_index +=1
    return new_nums
    


    '''
Stepping Stone #2

Given an array of integers, and two pointers, iterate through arr with one pointer and move one pointer only when the value is > 0. Return the value of the second pointer. Assume that the second pointer starts at 0.

 


Example

1) nums = [0,1,0,3,12] —> 3
2) nums = [1,3,12] —> 3
3) nums = [1,3,12, 0, 0] —> 3
4) nums = [0, 0] —> 0



'''

def move(nums):
    slow_ptr = 0
    p = 0
    while p < len(nums):
        if nums[p] > 0:
            slow_ptr += 1
        p += 1
    return slow_ptr



'''
#Problem 
#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements. Do this in-place. 

#Example 
# 1) nums = [0,1,0,3,12] --> [1,3,12,0,0]


** pseudocode **

create zeros counter
create index
while index is less than length of nums:
    if the element is 0, 
        remove from list            # changes length
        increment zeroes counter
    else:
        increment index
for number of times in zeros counter:
    append a zero onto nums
return nums

'''

def move(nums):
    zeroes = 0
    u = 0
    while u < len(nums):
        if nums[u] == 0:
            nums.pop(u)
            zeroes += 1
        else:
            u += 1
    for each in range(u-1):
        nums.append(0)
    return nums