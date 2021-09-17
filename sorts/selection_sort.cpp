/*  Selection Sort:

** pseudocode **
create input_value and set to 0
create array_size and set to 0
while input_value is not null
    print statement requesting value to be input
    increment array_size

create largest_element variable
create index_value variable
create swap_value variable
create counter and set to 0
X create swap_index variable
X create current_index variable and set to 0  
create subarray_index variable to initial size of array - 1
while subarray_index > 0:
    set largest element to first element
    for each element up to subarray index; increment current_index:
        if larger than largest element variable:
            set largest_element to new value
            set swap_index to current_index
    set swap_value to value of largest_element
    set element[swap_index] to element[subarray_index]
    set element[subarray_index] to swap_value
    decrement subarray_index
*/


#include <iostream>
using namespace std;

int** createArray();
void printArray(int*, int*);

int main()
{
    int** ptrArray = createArray();
    printArray(ptrArray[0], ptrArray[1]);
    delete [] ptrArray;
    ptrArray = nullptr;

    // int largest_value;
    // int largest_index;
    // int swap_holder;
    // int counter = 0;
    // int subarray_end = **ptrArray[1];

    // cout << "Element: " << subarray_end;

    // while (subarray_end > 0)
    // {
    //     largest_value = *ptrArray[0][0];
    // }

    return 0;
}


int** createArray()
{
    // Get array length from user.
    int* length = new int;
    
    cout << "Length of array: " << endl;
    cin >> *length;

    // Get data from user and store in an array.
    int input;
    int* array = new int[*length];
    for (int j=0; j<*length; j++)
    {
        cout << "Input an integer." << endl;
        cin >> input;           
        // cout << "Your number: " << input << endl;
        array[j] = input;
    }

    // Create array of arrays to return data.
    int** array_data = new int*[2];
    array_data[0] = array;
    array_data[1] = length;

    return array_data;
}


void printArray(int* array, int* length)
{
    // Print an array.
    int i;
    for (i=0; i<=*length-2; i++)
    {
        cout << array[i] << ", ";
    }
    cout << array[i];
    cout << endl;
}




/* 
*** Pointers ***
NOTE:   * has so far been used for:
    x * y					multiplication
    int *ptr = nullptr;		definition of a pointer
    *ptr = 100;				indirection operator

◊ &array however, points to the entire array
◊ array is a pointer that just points to the first element
◊ &array + 1 points to the address increment of the whole array, plus one more entry
◊ array + 1 just points to the second element, array[1]

• Pointer variable	int	*ptr	Used to define a pointer
• Address operator		&var	Used on the original variable to give access to it’s address
• Indirection operator	*ptr	Used on a pointer to refer to the value
• Initialization	

§ Uses of &
	int &ref = x;
		¬ reference operator
		¬ in a declaration (or as a parameter), it creates a reference variable
		¬ ref is an alias for x
	int *p = &x
		¬ address operator
		¬ p stores the address of x

*/