'''
A prime number is a number that cannot be formed by multiplying any numbers but 1, and itself. Another way of saying that is that a prime number is only divisible by 1, and itself. Prime numbers are not "composed" of any other numbers, and so we say that numbers that are not Prime, are Composite. All composite numbers can be decomposed into prime factors.

Prompt:
Count the number of prime numbers less than a non-negative number, n.

Given 10, your countPrimes solution should return 4
Given 20, your countPrimes solution should return 8

1 does not count as a prime number.

This problem is best divided into two functions:

    Counting Primes - countPrimes()
    Determining Primality - isPrime()

'''


def countPrimes(n):
    '''Counts all prime numbers between 2 and the input number.
    Assumes n is an int. Returns int.'''
    counter = 0
    subject = n - 1
    while subject > 1:
        if isPrime(subject):
            counter += 1
        subject -= 1
    return counter


def isPrime(i):
    '''Tests if input number is prime. Returns bool.'''
    counter = 2
    while counter < i:
        if not (i % counter):
            return False
        else:
            counter += 1
    return True



print("Input an integer:")
n = input()
n = int(n)
print(countPrimes(n))

