#include <iostream>
using namespace std;

/*
Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:
Given numRows = 5,
Return:

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]

Recursion:
Would probably use a function within a function
Would start with 5, then whittle down to 1
Would take the answer returned from a lower number to determine higher
Would take 1 as the base cases

numRows = 4
prev = [1,2,1]
#     [1,3,3,1]
[1, prev[0] + prev[1], prev[1] + prev[2], 1]


numRows = 5
prev = [1,3,3,1]
#     [1,4,6,4,1]
[1, prev[0] + prev[1], prev[1] + prev[2], prev[2] + prev[3], 1]


Pseudocode:
    Initial: 1
            1,1
    Algo:
        Start row with 1
        Sum each pair from previous row
        End with a 1

    Code:
    function (n):
        accumuator = []
        while i <= n:


    function(n):
        while n > 1:
            list = function(n-1)
        if n = 1
            return [1]
        if n = 2
            list = [[1],[1,1]]
            return list
        if n > 2
            next_list = [1]
            for i in range(len(list[-1])-1):
                coeff = list[i] + list[i+1]
                next_list.append(coeff)
            next_list.append(1)
            list.append(next_list)
            return list        

    Example, n = 5
        call function(5)
        call function(4)
        call fn(3)
        call fn(2)
        call fn(1)
        return fn(1): [1]
        return fn(2): [[1],[1,1]]

    n = 3
        list_of_lists = [[1],[1,1]]


*/

int** pascal_triangle(int n) {
    if (n == 1) {
        int** arr1 = new int*[1];
        arr1[0] = new int[1];
        arr1[0][0] = 1;
        return arr1;
    }
    else if (n == 2) {
        int** arr2 = new int*[2];
        arr2[0] = new int[1];
        arr2[0][0] = 1;
        arr2[1] = new int[2];
        arr2[1][0] = 1;
        arr2[1][1] = 1;
        return arr2;
    }
    else {
        int** list_of_lists = pascal_triangle(n-1);
        int** arr3 = new int*[n];

        // Copies previous triangle into array with more space available.
        for (int i=0; i<n-1; i++) {
            arr3[i] = list_of_lists[i];
        }

        // Adds new row to triangle using the previous row.
        arr3[n-1] = new int[n];
        arr3[n-1][0] = 1;
        for (int k=0; k<n-2; k++) {
            arr3[n-1][k+1] = arr3[n-2][k] + arr3[n-2][k+1];
        }
        arr3[n-1][n-1] = 1;

        return arr3;
    }
}

void print_pascal(int** triangle, int n) {
    for (int p=0; p<n; p++) {
        cout << endl;
        for (int q=0; q<=p; q++) {
            cout << triangle[p][q];
        }
    }
    cout << endl;
}

void delete_triangle(int** triangle, int n) {
    for (int r=0; r<n; r++) {
        delete [] triangle[r];
        triangle[r] = nullptr;
    }
    delete [] triangle;
    triangle = nullptr;
}


int main() {
    int n = 25;
    int** output = pascal_triangle(n);
    print_pascal(output, n);
    return 0;
}




