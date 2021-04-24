'''
# Find the largest number in a list. Assume all numbers are 0 or greater.

#Examples
#1) [10,9,8,7,6,5,4,3,2,1] --> 10
#2) [1,2,3,4,5,6,7,8,9,10] --> 10
#3) [0,0,0,0,0] --> 0


** pseudocode **

create greatest = 0
for s in range(len(list)):
    if list[s] is greater than greatest:
        set greatest equal to list[s]
return greatest
    


'''

def longestUniqueSubsttr(nums): 
    greatest = 0
    for s in range(len(nums)):
        if nums[s] > greatest:
            greatest = nums[s]
    return greatest


'''
# Return a set of all substrings which contain only unique letters. The resulting order may be different than the examples. 

#Examples:
#1) "abcabcbb" --> {'ab', 'b', 'c', 'ca', 'cb', 'a', 'cab', 'bc', 'bca', 'abc'}
#2) "bbbb" --> {'b'}
#3) "pwwkew" --> {'p', 'ke', 'wke', 'e', 'ew', 'kew', 'pw', 'w', 'wk', 'k'}


** psudocode **

create a sub_string set
for t in range(len(string)):
    # starting from index t, iterate from there, 
        # checking if each substring is in sub_string set, 
        # add the substring if not
    # also check if new letter is in previous substring, 
        # change repeat flag to true, if so
    create repeat = false
    create iterator = 1
    while repeat equals false and iterator + t is < len(string):
        if string[t+iter] is in string[t: t+iter]:
            set repeat = true
        elif string[t: t + iter] not in sub_string:
            add it to the set
        increment iterator
return sub_strings
        

"abcabcbb"

a
if a is not in ''
if a is not in sub_strings
b
if b is not in a
if ab is not in sub_strings



'''

def longestUniqueSubsttr(str): 
    sub_strings = set()
    for t in range(len(str)):
        repeat = False
        u = 0
        while not repeat and (t + u) < len(str):
            # print(t)
            # print(u)
            # print(str[t+u] + ", " + str[t: t+u])
            if str[t+u] in str[t: t+u]:
                repeat = True
            elif str[t: t+u+1] not in sub_strings:
                sub_strings.add(str[t: t+u+1])
            # print(sub_strings)
            u += 1
    return sub_strings


longestUniqueSubsttr("abcabcbb")
