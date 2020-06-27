
'''
where k is non-negative.

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

begin for loop at len(list) - k
append into new list 
begin again at front of list and end at len(list) - k - 1

for i in len(array) - (k + 1):
    remove array[i]
    append to array



'''


def rotate_array(input_array, k):
    for i in range(len(input_array) - k):
        input_array.append(input_array.pop(0))


testArray = [1,2,3,4,5,6,7]
rotate_array(testArray, 3)
print(testArray)  