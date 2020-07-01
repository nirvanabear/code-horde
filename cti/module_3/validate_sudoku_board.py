'''

Author: Prakash Acharya

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

(A partially filled sudoku which is valid.)

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

'''


list_of_lists1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

list_of_lists2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]





def is_valid_sudoku(list_of_lists):
    if validate_rows(list_of_lists):
        if validate_columns(list_of_lists):
            if validate_boxes(list_of_lists):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def validate_rows(list_of_lists):
    for i in range(0, len(list_of_lists)):
        num_list = []
        for char in list_of_lists[i]:
            if char != '.' and char in num_list:
                return False
            elif char not in num_list:
                num_list.append(char)
    return True


def validate_columns(list_of_lists):
    list_of_columns = []
    i = 0
    while i < 9:
        temp_list = []
        for j in range(0, len(list_of_lists)):
            temp_list.append(list_of_lists[j][i])
        list_of_columns.append(temp_list)
        i += 1
    return validate_rows(list_of_columns)


def validate_boxes(list_of_lists):  
    list_of_boxes = []
    for m in range(3):
        for n in range(3):
            # m = 0,1,2
            p = m * 3
            q = p + 3
            # p = 0,3,6
            # q = 0,3,6
            # n = 0,1,2
            r = n * 3
            s = r + 3
            temp_list = []
            for i in range(p, q):
                for j in range(r, s):
                    temp_list.append(list_of_lists[i][j])
            print(temp_list)
            list_of_boxes.append(temp_list)
    return validate_rows(list_of_boxes)


print(is_valid_sudoku(list_of_lists2))





# def validate_sudoku_board(board):
#   digits = 
#   for row in board:
#     for entry in row:
#       if not ".":



# # def validate_boxes(list_of_lists):
# temp_list = []
# for i in range(3):
#   for j in range(3):
#     if not ".":
#       temp_list.append(list_of_lists[j][i])
#   # list_of_columns.append(temp_list)
# print(temp_list)

# temp_list = []
# for i in range(4,7):
#   for j in range(4,7):
#     if not ".":
#       temp_list.append(list_of_lists[j][i])
#   # list_of_columns.append(temp_list)
# print(temp_list)

# for m in range(3):
#   for n in range(3):
#     # m = 0,1,2
#     # n = 0,1,2
#     p = m * 3
#     q = p + 3
#     # p = 0,3,6
#     # q = 0,3,6
#     r = n * 3
#     s = q + 3
#         temp_list = []
#     for i in range(p, q):
#         for j in range(0, 3):
#             temp_list.append(list_of_lists[i][j])
#     print(temp_list)
#     list_of_boxes.append(temp_list)





#         temp_list = []
#     for i in range(, 3):
#         for j in range(3, 6):
#             temp_list.append(list_of_lists[i][j])
#     list_of_boxes.append(temp_list)
#     print(temp_list)


'''
for 0,1,2
  for 0,1,2
'''
