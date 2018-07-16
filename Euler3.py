'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


'''

import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

bigNum = 600851475143

primes = []

for i in range(1,round(600851475143 / 2), 2):
    if is_prime(i) and bigNum % i == 0:
        primes.append(i)
        print(i)














































