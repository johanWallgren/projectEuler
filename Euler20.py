'''

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''

def factorial(n):
    val = 1
    for i in range(n,1,-1):
        val = val * i

    val = str(val)
    return val

strVal = factorial(100)
val = 0
for i in range(len(strVal)):
    val = val + int(strVal[i])


print(val)