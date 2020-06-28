def valid_anagram(s,t):
    counter = 0
    for letter in s:
        index = t.rfind(letter)
        if index == -1:
            return False
        else:
            counter += 1
    
