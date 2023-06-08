'''
Given an integer array, move all elements that are 0 to the left while maintaining the order of other elements in the array. The array has to be modified in-place.

int v[] = {1, 10, 20, 0, 59, 63, 0, 88, 0};
'''

# does length of array need to be maintained?
# any negative numbers?
# can additional outside variables be used?

def to_the_left(target, array):
    '''Move all instances of a certain value to the 
    left of the array.'''
    # iterate down the array using range
    for i in range(len(array)):
        if array[i] == target:
            # for loop
            for j in range(i-1, -1, -1):
                # print(j)
                array[j+1] = array[j]
            array[0] = target
    return array

    # if match:
    # store previous item in current location
    # store each item in the next spot up until back at 0
    # then change index 0 to target value

if __name__ == "__main__":
    array1 = [1, 10, 20, 0, 59, 63, 0, 88, 0]
    print(to_the_left(0,  array1))
