
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Examples:

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0


** pseudocode **
for index in range of array length:
    if element == target:
        return index
    elif element > target:
        return index - 1

'''


def find_index(sorted_list, target):
    for s in range(len(sorted_list)):
        if sorted_list[s] >= target:
            return s
        # elif sorted_list[s] > target:
        #     return s - 1
    return len(sorted_list)
