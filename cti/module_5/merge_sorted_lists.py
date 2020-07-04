'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.



Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]



** pseudocode **
for each in nums2
    if > 0:
        append to nums1
sort nums1

'''

def merge_sorted_lists(nums1, nums2):

    nums1[:] = [item for item in nums1 if item != 0]
    print("initial nums1: " + str(nums1))

    for each in nums2:
        if each > 0:
            nums1.append(each)
    nums1.sort()


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

merge_sorted_lists(nums1, nums2)

print(nums1)

