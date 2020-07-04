
'''
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than or equal to the last integer of the previous row.

Example:
Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]


Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem



** pseudocode **
for i in range of number of rows - 1:
    if matrix[i + 1][0] >= target:
        for j in range of length of row:
            if element == target:
                return 1
            if element > target:
                return 0


'''


def matrix_search(matrix, target):
    for i in range(len(matrix) - 1):
        if matrix[i + 1][0] >= target:
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return 1
                if matrix[i][j] > target:
                    return 0
    for k in range(len(matrix[-1])):
        if matrix[-1][k] == target:
            return 1
        if matrix[-1][k] > target:
            return 0
    return 0


