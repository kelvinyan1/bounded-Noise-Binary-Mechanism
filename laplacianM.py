import numpy as np
import math

def samples(epsilon, T):
    return np.random.laplace(0, math.log2(T)/epsilon , T)




def testLap(epsilon,T):
    numbers = samples(epsilon,T)
    logT = int(math.log2(T))
    return np.sum((-numbers).argsort()[:logT])
