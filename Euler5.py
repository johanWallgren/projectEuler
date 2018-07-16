
'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


'''

divVals = list(range(3,21))

remZero = False
testVal = 2520

while remZero == False:
    remZero = True
    for divisor in divVals:
        if testVal % divisor != 0:
            remZero = False
            break
    testVal += 1

print(str(testVal -1))