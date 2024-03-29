#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int what() {
    return 0;
}

int array_to_pointer(int* array, int k) {
    printf("Array pointers decay to basic pointers when used as an argument for a function.\n");
    printf("Location plus one returns the size of the int pointer which ends up being some multiple of 4 larger than the size of the array.\n");
    int* len = *(&array + 1);
    printf("Addresses are the same as some new location past the end of the array and array[0].\n");
    cout << len << endl;    // 0x7ff7bdcc42b0
    cout << array << endl;  // 0x7ff7bdcc4280
                            // 48
    printf("Size of int pointer inside function.\n");
    int num = *(&array + 1) - array;
    cout << num << endl;
    return 0;
}


/*
	• Make sure that function returns pointer to an object that still exists after the function ends
		¬ arrays or variables defined within a function are destroyed when it ends
		¬ any pointer to such an array will have nothing to point to
	• Pointers should be returned from functions that
		¬ point to an item passed in as a function
		¬ points to a dynamically allocated chunk of memory 
			◊ this can be created inside the function
			◊ memory remains allocated until delete is used, so it persists after a function ends */
char *findNull(char *str)
{
    char *ptr = str;
    while (*ptr != '\0')
        ptr++;
    return ptr;
}

int* returnArray(int array[]) {
    for (int i=0; array[i]; i++) {
        cout << array[i] << endl;
    }
    return array;
}


int main() {
    what();

    char** list_of_lists1 = new char*[9];
    // This notation requires C++11
    // list_of_lists1[0] = new char[9] {'5','3','.','.','7','.','.','.','.'};
    printf(R"(Howdy 'partner'.)");
    

    int arr[] = {1,2,3,4,5,6,7};
    printf("Arrays that are in the scope they are defined in can use sizeof()\n");
    int arrSize = sizeof(arr)/sizeof(arr[0]);
    cout << arrSize << endl;


    int array[] = {1,2,3,4,5,6,7,8,9,1,2,3,4,5,65,1,2,3,4,5,5,6,7,8,9,3,6,4,54,3,34,5,3,5,6,4,5,3,3,45,6,4,5,6,7,8,67,4,3,2,22,2,3,4,5,56,6,7,7,78,8,9,97,6,5,5,5,4,3,3,2,2,2,4,5,5,6,5,45,6};

    array_to_pointer(array, 3);
    int len = *(&array + 1) - array;
    printf("Size of entire array.\n");
    cout << len << endl;

    int* add = *(&array + 1);
    printf("Addresses are the same as array[1] and array[0].\n");
    cout << add << endl;    // 0x7ff7bdcc429c
    cout << array << endl;  // 0x7ff7bdcc4280
                            // 28

    printf("Reference operator allows variables to point to same location.\n");
    int julie = 12;
    int &agatha = julie;
    int* samantha = nullptr;
    int* charlotte = nullptr;
    printf("Changes to each variable affect the other.\n");
    cout << agatha << endl;
    julie += 8;
    cout << julie << endl;
    cout << agatha << endl;
    agatha += 5;
    cout << julie << endl;
    cout << agatha << endl;
    printf("They point to the same location.\n");
    cout << &julie << endl;         // 0x7ff7bea7f2d8
    cout << &agatha << endl;        // 0x7ff7bea7f2d8
    cout << endl;

    printf("Array as a pointer.\n");
    int array2[] = {1,2,3,4,5,6,7};
    cout << &array2 << endl;
    cout << &array2[1] << endl;
    printf("Gives answer in bytes.\n");
    cout << sizeof(array2) << endl;
    printf("Does NOT give answer in bytes, but in array locations.\n");
    cout << &array2[1] - &array2[0] << endl;
    printf("Value of the same location.\n");
    cout << *array2 << endl;
    cout << array2[0] << endl;
    printf("Regular arithmetic on the values pointed to.\n");
    cout << *array2 + 8 << endl;
    cout << *(array2 + 6) << endl;
    printf("Past the end of the array. Contents are from random programs.\n");
    cout << *(array2 + 12) << endl;  // -1096289248
    cout << *(array2 + 13) << endl;  // 32759
    printf("These are null pointers.\n");
    cout << &samantha << endl;      // 0x7ff7bea7f2c8
    cout << charlotte << endl;      // 0x0
    printf("Address operator on a pointer is the same as just the pointer.\n");
    cout << &array2 << endl;         // 0x7ff7bea7f2e0
    cout << array2 << endl;          // 0x7ff7bea7f2e0
    printf("But act differently with addition and indirection.\n");
    cout << &array2 + 1 << endl;     // 0x7ff7bea7f2fc
    cout << &array2[7] << endl;      // 0x7ff7bea7f2fc
    cout << array2 + 1 << endl;      // 0x7ff7bea7f2e4
    cout << &array2[1] << endl;      // 0x7ff7bea7f2e4
    printf("Even more different, because first one has no value.\n");
    cout << *(&array2 + 1) << endl;  // 0x7ff7bea7f2fc
    cout << *(array2 + 1) << endl;   // 2
    printf("However, * casts address to an int* to be used in math with another int*, ie, the original array pointer.\n");


    int *iptr = nullptr;

    int five = 5;
    string fiveStr = to_string(five);
    const char* fiveChar = fiveStr.c_str();
    cout << fiveChar << endl;

    // Needs C++11 to properly initialize
    // without .push_back()
    // vector<int> nums;
    // nums = {4,1,2,1,2};

    cout << "Here's a pointer return with the for loop trick." << endl;
    int* arrPtr = returnArray(arr);
    cout << "for loop trick doesn't work for an int array" << endl;
    for (int j=0; j<(sizeof(arr)/sizeof(int)); j++) {
        cout << arrPtr[j] << ", ";
    }
    cout << "Only works for c-string with \\0 terminator." << endl;
    cout << endl;

    cout << "Array of Arrays" << endl;
    int **arrayArray = new int*[3];
    arrayArray[0] = new int[1];
    arrayArray[1] = new int[2];
    arrayArray[2] = new int[2];

    arrayArray[0][0] = 1;
    arrayArray[1][0] = 1;
    arrayArray[1][1] = 1;
    arrayArray[2][0] = 7;
    cout << arrayArray[1][0] << arrayArray[1][1] << endl;

    // Set an int* pointer equal to another int* pointer.
    // Deallocate memory before reassigning.
    delete [] arrayArray[0];
    arrayArray[0] = arrPtr;
    for (int k=0; k<(sizeof(arr)/sizeof(int)); k++) {
        cout << arrayArray[0][k];
    }
    cout << endl;
    cout << arrayArray[2][1] << endl;

    cout << "Indexing and indirection operator (below) access the value.
    " << endl;
    *(*(arrayArray + 2)+ 1) = 8;
    cout << arrayArray[2][1] << endl;
    delete [] arrayArray[2];
    *(arrayArray + 2) = arrPtr;
    cout << arrayArray[2][1] << endl;

    return 0;
}