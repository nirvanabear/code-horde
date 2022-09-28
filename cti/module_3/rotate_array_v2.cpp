#include <iostream>
using namespace std;
/*
where k is non-negative.
(code works for positive and negative k)

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


*/

void rotate_array(int* array, int len, int k) {
    if (k > 0) {
        for (int i=0; i<k; i++) {
            int placeholder = array[len-1];
            for (int j=len-1; j>0; j--) {
                array[j] = array[j-1];
            }
            array[0] = placeholder;
        }
    }
    else {
        for (int i=0; i>k; i--) {
            int placeholder = array[0];
            for (int j=0; j<len-1; j++) {
                array[j] = array[j+1];
            }
            array[len-1] = placeholder;
        }
    }

}

void print_array(int* array, int len) {
    for (int m=0; m<len; m++) {
        cout << array[m] << ", ";
    }
    cout << endl;    
}

int main() {
    int array[] = {1,2,3,4,5,6,7};
    int len = sizeof(array) / sizeof(array[0]);
    rotate_array(array, len, -3);
    print_array(array, len);

    int array2[] = {1,2,3,4,5,6,7};
    len = sizeof(array2) / sizeof(array2[0]);
    rotate_array(array2, len, 3);
    print_array(array2, len);    

    return 0;
}

