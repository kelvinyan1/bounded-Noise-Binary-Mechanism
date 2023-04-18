import boundedNoise
import math
import numpy as np

def testBN(epsilon, delta, T):
    numbers = []
    for _ in range(1,T):
        factor = 4*math.sqrt(  math.log2(T) * math.log2(1/delta) )/epsilon
        newvalue = factor*boundedNoise.sample()
        numbers.append(newvalue)

    numbers = np.array(numbers)

    return np.sum((-numbers).argsort()[:int(math.log2(T))])
