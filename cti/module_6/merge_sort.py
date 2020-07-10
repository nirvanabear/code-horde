
'''
Given a list of unsorted numbers, sort them using the Merge Sort algorithm. 

Don't use the built-in sorted or list.sort() methods - the goal of this is to understand and implement the merge sort algorithm.


** pseudocode **

    divide array into halves
    sort each half
        divide array into halves
        sort each half
            divide array into halves
            sort each half              
                merge the halves into temporary array
                copy array into the original




    if len(nums) = 1
        return nums

    else:
        # divide array into halves
        pivot = len(nums) // 2
        half1 = nums[:pivot]
        half2 = nums[pivot + 1:] 
        half1 = merge_sort(half1)
        half2 = merge_sort(half2)
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
            temp_array.append(half2[j:])
        else:
            temp_array.append(half1[i:])
        return temp_array





'''

# recursive version:

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    else:
        # divide array into halves
        pivot = len(nums) // 2
        half1 = nums[:pivot]
        half2 = nums[pivot:] 
        print("push: " + str(half1) + ", " + str(half2))
        half1 = merge_sort(half1)
        half2 = merge_sort(half2)
        print("pop: " + str(half1) + ", " + str(half2))
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

array = [1,2,8,4,5,6]
print(merge_sort(array))
