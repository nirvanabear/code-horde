'''
    Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8} 
    Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

    Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8} 
    Output: arr3[] = {4, 5, 7, 8, 8, 9} 
'''

# are they presorted, are they of different lengths, do they have 
# negative numbers?, fractions?, any nulls?, any non-numbers?

def merge_arrays(list1, list2):
    '''Merge two presorted lists of digits.'''
    # Create output list to add to
    output = list()
    # Create counter for second list
    i = 0
    j = 0
    # Check longer list
    if len(list1) >= len(list2):
        first = list1
        second = list2
    else:
        first = list2
        second = list1
    # Iterate through longer list
    while (i < len(first)) and (j < len(second)):
    # for j in range(len(first)):
    # If list1 item is less than list2 item, append to output
        if first[i] < second[j]:
            output.append(first[i])
            i += 1
        # And list2 counter is not greater than len(list2)
    # Else if while list2 item is less than list1, append to output
        elif first[i] == second[j]:
            output.append(first[i])
            i += 1
            output.append(second[j])
            j += 1
        # zncrement list2 counter
        else:
            output.append(second[j])
            j += 1
    if i < len(first):
        back = first[i:]
        # print(back)        
        output = output + back
    if j < len(second):
        back = second[j:]
        output = output + back
    # Return output list
    return output

if __name__ == "__main__":
    list1 = [1, 3, 4, 5] 
    list2 = [2, 4, 6, 8]
    list3 = [ 5, 8, 9]
    list4 = [4, 7, 8]
    print(merge_arrays(list1, list2))
    print(merge_arrays(list3, list4))
