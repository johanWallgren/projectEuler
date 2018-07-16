'''

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
import math

for a in range(500):
    for b in range(500):
        c = math.sqrt(a**2 + b**2)
        if a + b + c == 1000:
            print(a,b,c)
            print(int(a*b*c))

