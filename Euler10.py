'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
from math import sqrt; from itertools import count, islice

def checkIfPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

primeSum = 0
for val in range(1,2000000,1):
    if checkIfPrime(val):
        primeSum += val

print(primeSum)


#sum=0;
#for i in range(1,int(2e6),2):
#    if checkIfPrime(i):
#        sum += i