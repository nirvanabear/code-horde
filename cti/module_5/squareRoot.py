
'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Do not use any built square root functions.

Example 1:

Input: 4
Output: 2


Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.


** pseudocode **
counter = 1
found = false
while not found:
    if counter^2 > target:
        found = true
    else:
        counter++
return counter - 1



'''



def squareRoot(num):
    counter = 1
    found = False
    length = 0
    for digit in str(num):
        length += 1
    # print(length)
    if length > 1:
        # denominator = (length - 1) // 2       ## EDIT: removed /
        denominator = (length - 1) / 2
        counter = int(10 ** denominator)
    # print(counter)
    while not found:
        if counter**2 > num:
            found = True
            counter -= 1
        else:
            counter += 1
        # print(counter)
    return counter

replit = 1000000000000000
print(squareRoot(replit))



# def squareRoot(num):
#     for i in range(10000000000):
#         if i**2 > num:
#             i -= 1
#             return i
