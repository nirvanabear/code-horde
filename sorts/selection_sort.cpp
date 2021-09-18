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
    
    int largest_value;
    int largest_index;
    int swap_holder;       
    int subarray_end = *ptrArray[1] - 1;

    while (subarray_end > 0)
    {
        largest_value = ptrArray[0][0];
        largest_index = 0;
        for (int i=0; i<=subarray_end; i++)
        {
            if (ptrArray[0][i] > largest_value)
            {
                largest_value = ptrArray[0][i];
                largest_index = i;
            }
        }
        ptrArray[0][largest_index] = ptrArray[0][subarray_end];
        ptrArray[0][subarray_end] = largest_value;
        subarray_end--;
    }

    printArray(ptrArray[0], ptrArray[1]);

    delete [] ptrArray;
    ptrArray = nullptr;

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
    for (i=0; i<*length-1; i++)
    {
        cout << array[i] << ", ";
    }
    cout << array[i];
    cout << endl;
}




