import math
import random



Z_f = 0.340294238275125928517229 # from more accurate calculator

def sample():
    minimum = -1
    maximum = 1
    upperbound_pdf = 1/Z_f
    while True:
        p = random.uniform(minimum, maximum)
        z = random.uniform(0, upperbound_pdf)
        try:
            prob = pdf(p)
            if z <prob:
                return p
        except OverflowError as e:
            return p
            

def pdf(v):
    return (math.e)**((1/(1-v**2))**2)/Z_f
