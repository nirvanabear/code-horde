'''

Author: Prakash Acharya

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

(A partially filled sudoku which is valid.)

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


Pseudocode:
    Validate each region in turn:
        Rows
        Columns
        Sub-boxes


        (how to iterate only one time through each row)
        (no repeats, no decimals, nothing over or under, correct length)

    if len of sudoku not equal 9, Fail

    For each in the sudoku:
        if len does not equal 9, Fail
        initialize new dictionary
        for each entry:
            pop from dict, with "" as default return value
                if returns anything but "" or ".", Fail
                if returns "", add to dict

    for index in range of list length
        initialize dictionary
        for each in sudoku
            pop list[index] from dict...

    BAD: Actually, I'm really liking setdefault for this, as it always
    returns a value, with no error option.


    for number1 0 through 2
        for number2 0 through 2
            initialize dictionary
            for index1 0 through 2, plus number1 (rows)
                for index2 0 through 2, plus number2 (columns)
                    pop list[index][index] from dict...
    
    Example:
        00 01 02 10 11 12 20 21 22

for numRow in range

0
0: 012
1: 012
2: 012

1
0: 345
1: 345
2: 345

2
0: 678
1: 678
2: 678

0
3: 012
4: 012
5: 012


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


def check_rows(sudoku):
    row_count = 0
    for row in sudoku:
        if len(row) != 9:
            status = False
            print("row count failed")
            return status
        check = {}
        for entry in row:
            if entry.isnumeric():
                if check.pop(entry, "Empty") == "Empty":
                    check[entry] = "Entered"
                else:
                    status = False
                    print(f"check_rows:    {entry} at {row} failed")
                    return status
    status = True
    return status

def check_columns(sudoku):
    if len(sudoku) != 9:
        print("sudoku size failed")
        status = False
        return status
    for i in range(9):
        check = {}
        for row in sudoku:
            if row[i].isnumeric():
                if check.pop(row[i], "Empty") == "Empty":
                    check[row[i]] = "Entered"
                else:
                    status = False
                    print(f"check_columns: {row[i]} at {row} failed")
                    return status

            # if check.pop(row[i], ".") != ".":
            #     print(f"{row[i]} failed")
            #     status = False
            #     return status
    status = True
    return status

def check_blocks(sudoku):
    for t in range(3):
        for u in range(3):
            check = {}
            for i in range(t*3, 3 + (t*3), 1):
                for j in range(u*3, 3 + (u*3), 1):
                    if sudoku[i][j].isnumeric():
                        if check.pop(sudoku[i][j], "Empty") == "Empty":
                            check[sudoku[i][j]] = "Entered"
                        else:
                            status = False
                            print(f"check_blocks:  {sudoku[i][j]} at {i}, {j} failed")
                            return status
            # Prints dict of all unique values in a single block.
            # print(f"{check.keys()}")
    status = True
    return status

def check_status(sudoku):
    rows_checked = check_rows(sudoku)
    columns_checked = check_columns(sudoku)
    blocks_checked = check_blocks(sudoku)
    print("******")
    print(f"check_rows:    {rows_checked}")
    print(f"check_columns: {columns_checked}")
    print(f"check_blocks:  {blocks_checked}")
    if rows_checked == False or columns_checked == False or blocks_checked == False:
        print("Invalid Sudoku :(")
    else:
        print("Sudoku OK!")
    print("***********")



if __name__ == "__main__":
    check_status(list_of_lists1)
    check_status(list_of_lists2)