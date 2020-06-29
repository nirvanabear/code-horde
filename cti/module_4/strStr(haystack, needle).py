'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


def strStr(haystack, needle):
    for m in range(len(haystack)):
        if haystack[m] == needle[0]:
            n = m
            match = True
            for letter in needle:
                if haystack[n] != letter:
                    match = False
                n += 1
            if match:
                print(m)
                return m
    print(-1)
    return -1