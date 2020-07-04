'''
Minimum Characters required to make a String Palindromic

You are given a string. The only operation allowed is to insert characters in the beginning of the string. Return the number of characters that are needed to be inserted to make the string a palindrome string


Examples:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2


** pseudocode **

input string
counter = 1
while not isPalindrome and string:
    string = string[:-1]
    counter += 1
return counter


'''


def minimumCharacters(word):
    inputStr = word
    counter = 0
    while not isPalindrome(inputStr) and inputStr:
        inputStr = inputStr[:-1]
        counter += 1
    return counter


def isPalindrome(words):
    front = 0
    rear = -1
    while front < len(words) and rear >= -len(words):
        while not words[front].isalpha():
            front += 1
        while not words[rear].isalpha():
            rear -= 1
        if words[front].lower() != words[rear].lower():
            return 0
        front += 1
        rear -= 1
    return 1

print(minimumCharacters('abc'))
