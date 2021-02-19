'''
Stepping Stone # 1

Output substrings of str_a (not exhaustive). Include original string in the output as well. 

 

Examples

1) str_a = “aba” —> [‘a’, ‘ab’, ‘aba’]

2) str_a  = “abab” —> [‘a’, ‘ab’, ‘aba’, ‘abab’]

 

*Note that the last values are not substrings of the string -- they are the string, but for the sake of simplicity and coding practice, just include them for this stepping stone. 


** psudocode **

create container substrings = []
for i in range(len(str_a)):
    take a slice of str_a from the start to the current index
    append the slice to the substrings container




'''

def repeatedSubstringPattern(s):
        """
        :type s: str
        :rtype: List[str]
        """
        substrings = []
        for i in range(len(s)):
                substrings.append(s[:i+1])
        return substrings

repeatedSubstringPattern("abab")


'''
Stepping Stone # 2

Can you append str_a to an empty string any number of times in order for the empty string’s final length to equate to the *exact* length of str_b. The result of the empty string and str_b do no need to equate in this example.

Note str_b could be any combination of characters in these examples, the important part is the length if str_b.

Imagine that str_a is the substring, and str_b is the resulting string of interest (except we only care about length, unlike the original problem). So instead of concatenating a substring to itself, you are concatenating str_a to itself.

Examples

1) str_a = “a” str_b = “aaa” —> true

2) str_a = “a” str_b = “aaaa” —> true

3) str_a = “aa” str_b = “aaa” —> false

4) str_a = “bbb” str_b = “bbb” —> true


** pseudocode **

create build string = ''
create shorter = True
create match = False
while build_string is smaller than str_b and shorter is true:
        append str_a to build
        if length of build is equal to str_b:
                set shorter = False
                set match = True
        elif build is greater than str_b:
                set shorter = False
        


        


'''

def repeatedSubstringPattern(str_a,str_b):
        """
        :type str_a: str
        :type str_b: str
        :rtype: bool
        """
        build = ""
        shorter = True
        match = False
        while shorter and len(build) < len(str_b):
                build = build + str_a
                if len(build) == len(str_b):
                        shorter = False
                        match = True
                elif len(build) > len(str_b):
                        shorter = False
        return match



'''
#Problem 
# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume that the given string consists of lowercase English letters only and it will not exceed 10000.

#Examples 

#1) "abab" --> True
#2) "aba" --> False
#3) "abcabcabcabc" --> True

** pseudocode **


'''

def repeatedSubstring(s):
        """
        :type s: str
        :rtype: bool
        """
        substrings = []
        for i in range(len(s) - 1):
                substrings.append(s[:i+1])
        j = 0
        match = False
        while not match and j < len(substrings):
                build = ""
                shorter = True
                while shorter and len(build) < len(s):
                        build = build + substrings[j]
                        if len(build) == len(s):
                                shorter = False
                                if build == s:
                                        match = True
                        elif len(build) > len(s):
                                shorter = False
                j += 1
        return match
