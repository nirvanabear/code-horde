'''
Inspired by Raymond Chen's post, say you have a 4x4 two dimensional array, write a function that rotates it 90 degrees. Raymond links to a solution in pseudo code, but I'd like to see some real world stuff.

[1][2][3][4]
[5][6][7][8]
[9][0][1][2]
[3][4][5][6]

Becomes:

[3][9][5][1]
[4][0][6][2]
[5][1][7][3]
[6][2][8][4]
'''

# how big, any limits on storage complexity,

import numpy as np

def rotate_matrix(matrix):
    '''Rotate all the values in a 2D-array 90 degrees around the center.
    Argument must be a square matrix.'''
    # For the example:
    # [i][j] -> [j][size - 1 - i]
    # check if matrix is square
    # create blank array of same size
    # for loop over rows
        # for loop over columns
        # store value in the transformed row/column
    if matrix.shape[0] != matrix.shape[1] or len(matrix.shape) > 2:
        return "Matrix must be square. Please input new matrix."
    output = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            output[j][matrix.shape[1] - 1 - i] = matrix[i][j]
    return output

# 0(n) == n^2

if __name__ == "__main__":
    matrix1 = np.array([[1,2,3,4],
[5,6,7,8],
[9,0,1,2],
[3,4,5,6]])
    print(rotate_matrix(matrix1))
