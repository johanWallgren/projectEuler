
import numpy as np

vals = list(range(1,101))
sumValsSquard = np.sum(vals) ** 2
sumSquaredVals = np.sum([i ** 2 for i in vals])
valDiff = sumValsSquard - sumSquaredVals

print(valDiff)