'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


Example 1:

Input: [2,2,1]
Output: 1



'''

def single_number_dict(numbers):
    check = {}
    for num in numbers:
        if not check.pop(num, None):
            check[num] = 1
    return check.keys()

def single_number_bitwise(numbers):
    check = 0
    for num in numbers:
        check ^= num
    return check

def single_number_math(numbers):
    check = set(numbers)
    return 2 * sum(check) - sum(numbers)

if __name__ == "__main__":
    numbers = [2,1,7,4,7,1,2]
    print(f"Dictionary: {single_number_dict(numbers)}")
    print(f"Bitwise: {single_number_bitwise(numbers)}")
    print(f"Math: {single_number_math(numbers)}")
