



'''

# iterarive version:

take list and divide
add to stack    add to stack
divide          divide

1,2,8,4,5,6

1,2,8   4,5,6

1,2     8   4,5     6

1   2   8   4   5   6


    ### this statement controls what gets pushed to the stack
    if len(nums) == 1:

[1,2,8,4,5,6]

push: [1, 2, 8], [4, 5, 6]
push: [1], [2, 8]
push: [2], [8]

pop: [2], [8]
pop: [1], [2, 8]

push: [4], [5, 6]
push: [5], [6]

pop: [5], [6]
pop: [4], [5, 6]
pop: [1, 2, 8], [4, 5, 6]

[1, 2, 4, 5, 6, 8]


** pseudocode **
push list elements onto stack2
pop two elements
merge sort into new list
push list onto stack2
continue until stack is empty
pop two elements from stack2
merge sort two elements
push onto stack1


def merge_sort(nums):
    pivot = len(nums) // 2
    stack1 = []
    for each in nums[:pivot]:
        initial = []
        initial.append(each)
        stack1.append(initial)
    stack2 = [] 
    for every in nums[pivot:]:
        starter = []
        starter.append(every)
        stack2.append(starter)   
    print("stack1: " + str(stack1))
    print("stack2: " + str(stack2) + "\n")


'''

# iterative version:

def merge_sort(nums):
    stack1 = []
    for each in nums:
        initial = []
        initial.append(each)
        stack1.append(initial)
    stack2 = []

    while not (len(stack1) == 1 and len(stack2) == 0):
        while len(stack1) > 1:
            half1 = stack1.pop()
            half2 = stack1.pop()
            merged_list = merge(half1, half2)
            stack2.append(merged_list)
        if len(stack1) == 1 and len(stack2) > 0:
            half1 = stack1.pop()
            half2 = stack2.pop()
            merged_list = merge(half1, half2)
            stack1.append(merged_list)
        print("stack2: " + str(stack2))
        while len(stack2) > 1:
            half1 = stack2.pop()
            half2 = stack2.pop()
            merged_list = merge(half1, half2)
            stack1.append(merged_list)
        if len(stack2) == 1 and len(stack1) > 0:
            half1 = stack2.pop()
            half2 = stack1.pop()
            merged_list = merge(half1, half2)
            stack2.append(merged_list)
        if len(stack2) == 1 and len(stack1) == 0:
            last = stack2.pop()
            stack1.append(last)
        print("stack1: " + str(stack1))
        
    
    print(stack1)
    print("stack1 length: " + str(len(stack1)))
    print(stack2)
    print("stack2 length: " + str(len(stack2)))

    if len(stack1) > 0:
        finished_sort = stack1
    else:
        finished_sort = stack2

    # print(finished_sort)

    return finished_sort[0]


def merge(half1, half2):
    i = 0
    j = 0
    temp_array = []
    # Start here: 
    # Never mind that you don't know where halves come from
    while i < len(half1) and j < len(half2):
        if half1[i] <= half2[j]:
            # add half1[i] to temp_array
            temp_array.append(half1[i])
            # i++
            i += 1
        else:
            # add half2[j] to temp_array
            temp_array.append(half2[j])
            # j++
            j += 1
    # add rest of array where i or j is less than len to temp_array
    if i == len(half1):
        temp_array.extend(half2[j:])
    else:
        temp_array.extend(half1[i:])

    return temp_array   



array = [1,2,8,7,34,6,3,65,2456,645,345,4,23,5,234,56,7,23,4,5,6]
print(merge_sort(array))