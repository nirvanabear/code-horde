
'''
Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice.
Note: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example:
>> arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
>> single_number(arr) # returns 4

OG Platform:  https://www.interviewbit.com/problems/single-number-ii/ 


** repl.it unit test **

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 35, in test_medium
    self.assertEquals(single_number(nums), 10)
AssertionError: 11 != 10

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 42, in test_huge
    self.assertEquals(single_number(nums), 10000)
AssertionError: 35328 != 10000

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 46, in test_large
    self.assertEquals(single_number(nums), 100)
AssertionError: 324 != 100

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 50, in test_medium
    self.assertEquals(single_number(nums), 10)
AssertionError: 2 != 10


** scratch paper **

    for t in range(len(nums) - 1):
        nums[t+1] = nums[t] ^ nums[t+1]
    # print(nums[-1])
    return nums[-1]


'''




def single_number(nums):

    nums[0] = int(bin(nums[0])[2:])
    for index in range(1, len(nums)):
        nums[index] = int(bin(nums[index])[2:]) + nums[index - 1]
    # print(nums)
    # print(bin(nums[-1]))
    string_sum = str(nums[-1])
    # print(string_sum)
    binary_result = "0b"
    for digit in string_sum:
        # print(each)
        if int(digit) % 3 == 1:
            # print(int(each) % 3 + 1)
            binary_result = binary_result + "1"
        else:
            binary_result = binary_result + "0"
    # print(binary_result)
    print(int(binary_result, 2))
    single_answer = int(binary_result, 2)
    return single_answer

'''


Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 44, in test_huge
    self.assertEquals(single_number(nums), 10000)
  File "/home/runner/unit_tests.py", line 22, in single_number
    print(int(binary_result, 2))
ValueError: invalid literal for int() with base 2: '0b01020121200002000'

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 48, in test_large
    self.assertEquals(single_number(nums), 100)
  File "/home/runner/unit_tests.py", line 22, in single_number
    print(int(binary_result, 2))
ValueError: invalid literal for int() with base 2: '0b121200120'

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 52, in test_medium
    self.assertEquals(single_number(nums), 10)
  File "/home/runner/unit_tests.py", line 22, in single_number
    print(int(binary_result, 2))
ValueError: invalid literal for int() with base 2: '0b2012'


'''

# def single_number(nums):

#     # nums[0] = int(bin(nums[0])[2:])
#     sums = 0
#     for index in range(len(nums)):
#         sums += int(bin(nums[index])[2:])
#     # print(nums)
#     # print(bin(nums[-1]))
#     string_sum = str(sums)
#     # print(string_sum)
#     binary_result = "0b"
#     for digit in string_sum:
#         # print(each)
#         one_or_zero = int(int(digit) % 3 == 0)
#         binary_result += str(one_or_zero)
#             # print(int(each) % 3 + 1)
#             # binary_result = binary_result + "1"
#         # else:
#         #     binary_result = binary_result + "0"
#     print(binary_result)
#     print(int(binary_result, 2))
#     single_answer = int(binary_result, 2)
#     return single_answer




if __name__ == "__main__":
    array1 = [2, 2, 2, 3]
    array2 = [1, 2, 3, 1, 10, 2, 3, 1, 2, 3]
    big_array = [1, 2, 3, 1, 2, 3, 1, 2, 3] * 5000
    big_array.append(20)
    single_number(big_array)


