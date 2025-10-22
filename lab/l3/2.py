import numpy as np
import matplotlib.pyplot as plt

sim = 100000

def tossThreeConsecutive(n, sim):
    total = np.array([])
    count = 0
    for i in range(1,sim+1):
        toss = np.random.random(n) < 0.5
        toss = toss[2:] & toss[1:-1] & toss[-2]
        count += np.any(toss)
        total = np.append(total, [count / i])
    plt.plot(range(1, sim + 1), total)

tossThreeConsecutive(20, 1000)
plt.ylim(0.4, 0.6)
plt.show()

