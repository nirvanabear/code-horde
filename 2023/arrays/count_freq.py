'''
Given an array which may contain duplicates, print all elements and their frequencies.

Examples: 

Input :  arr[] = {10, 20, 20, 10, 10, 20, 5, 20}
Output : 10 3
         20 4
         5  1

Input : arr[] = {10, 20, 20}
Output : 10 1
         20 2 
'''

# Is there a min/max length, is there a specified data type,
# are there mixed data types, input from command line? file?
# what about length 0

def count_freq(array):
    '''Count the frequency of all elements in an array'''
    # create dictionary
    frequencies = dict()
    # iterate down array
    for each in array:
    # first entry assigned value of 1
        if each in frequencies:
            frequencies[each] += 1
    # subsequent entries get value += 1
        else:
            frequencies[each] = 1
    # print in desired format
    # print(frequencies.items())
    for every in frequencies:
        print(str(every) + " " + str(frequencies[every]))
    print()
    # O(n): iterates over array once, checks a hashmap

if __name__ == "__main__":
    array1 = [10, 20, 20, 10, 10, 20, 5, 20]
    array2 = [10, 20, 20]
    count_freq(array1)
    count_freq(array2)

     