
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.


"A man, a plan, a canal, Panama."

index 0 & index -1
skip -1
index 0 & index -2
compare
index 1 & index -3


front = 0
rear = -1
while front < len(words):
    if not front.isalpha()
        increment 1
    if not rear.isalpha()
        decrement 1
    if front.lower() != rear.lower()
        return 0

return 1
    


for words 


'''


def isPalindrome( self ):

    front = 0
    rear = -1
    while front < len(words) and rear >= -len(words):
        # print(words[front])
        while not words[front].isalpha():
            print("skip: " + words[front])
            front += 1
        while not words[rear].isalpha():
            print("skip: " + words[rear])
            rear -= 1
        if words[front].lower() != words[rear].lower():
            print("front: " + words[front] + ", rear: " + words[rear]) 
            return 0
        front += 1
        rear -= 1
    return 1
  
test1 = "A man, a plan, a canal, Panama."
test2 = "hello"
test3 = "A nut for a jar of tuna."
test4 = 'Are we not pure? "No, sir!" Panama\'s moody Noriega brags. "It is garbage!" Irony dooms a man; a prisoner up to new era.'
print(isPalindrome(test4))
  