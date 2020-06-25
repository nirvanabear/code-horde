def last_factorial_digit(n):
    factorial = n
    for i in range(2, n):
        factorial *= i
    return factorial % 10