
'''
where k is non-negative.

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Solved:
9 min
Negative-version:
13 min

'''

# 
def rotate_array(array, k):
    for each in range(abs(k)):
        if k > 0:
            placeholder = array.pop()
            array = [placeholder] + array
        if k < 0:
            placeholder = array.pop(0)
            array =  array + [placeholder]
    return array

if __name__ == "__main__":
    print(rotate_array([1,2,3,4,5,6,7], -3))
