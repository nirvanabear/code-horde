
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


Example 1:

Input: [2,2,1]
Output: 1



'''


def single_number(integers):
    while True:
        try:
            item = integers.pop(0)
            integers.remove(item)
        except:
            print(item)
            return item


testList = [4,1,2,1,2]
# testList.remove(4)
print(testList)
single_number(testList)
