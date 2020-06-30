'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

-2147483648
2147483647


'''

def atoi(a):
    message = a.strip()
    if message[0] == '+' or '-':
        sign = message[0]
        message = message[1:]
    if not message[0].isnumeric():
        return 0        
    for q in range(len(message)):
        if not message[q].isnumeric():
            break   
    message = message[0:(q + 1)]
    final_message = int(sign + message)
    if final_message > 2147483647:
        final_messge = 2147483647
    if final_message < -2147483648:
        final_message = -2147483648
    print(final_message)
    return final_message


atoi("     -1234 now what?")
        


