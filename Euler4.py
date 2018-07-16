'''

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


'''
import numpy as np

i=0
prodVals = []
for val1 in range(100, 1000):
    for val2 in range(100, 1000):
        prodVals.append(val1 * val2)
        i += 1

prodVals = sorted(np.unique(prodVals), reverse=True)

i=1
isPal = False
while isPal == False:
    strProdVals = str(prodVals[i])
    i += 1
    if strProdVals[0:3] == strProdVals[3:6][::-1]:
        isPal = True

