


'''
In a product array puzzle problem we need to construct an array where the ith element will be the product of all the elements in the given array except element at the ith position.
Example

Input 

5

10 3 5 6 2

Output

180 600 360 300 900
'''

import math

# length max, 0 length, null positions?


def product_array(array):
    '''Constructs an array where the ith element will be the product of all the elements in a given array except the element at the ith position.
    '''
    # import math
    total_prod = math.prod(array)
    # make a new array
    output = list()
    # for each in array, divide total_prod by each
        # append to a new array
    for each in array:
        entry = total_prod / each
        output.append(entry)
    return output

    # O(n) == n


if __name__ == "__main__":
    array1 = [10, 3, 5, 6, 2]
    print(product_array(array1))
    