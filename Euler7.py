
'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?


'''
import numpy as np
from math import sqrt; from itertools import count, islice

def checkIfPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


foundPrimes = []
testValue = 2
while len(foundPrimes) < 10001:
    isPrime = checkIfPrime(testValue)
    if isPrime == True:
        foundPrimes.append(testValue)
    testValue += 1

print(np.max(foundPrimes))

























































