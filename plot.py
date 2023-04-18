import numpy as np
import matplotlib.pyplot as plt 
import boundedM
import laplacianM

x = np.linspace(10**3, 10**6, 10)
laps = []
bbs = []
for t in x:
    laps.append(laplacianM.testLap(0.1, int(t)))
    bbs.append(boundedM.testBN(0.1,0.001, int(t)))

plt.plot(x, laps)
plt.plot(x, bbs, 'r')
plt.show()