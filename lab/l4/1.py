import numpy as np
import matplotlib.pyplot as plt

def probNrUsi(n, sim):
    carDoors = np.random.randint(1, n+1, size=sim)
    finalDoors = np.random.randint(1, n+1, size=sim)

    win = np.cumsum(carDoors != finalDoors) / range(1, sim + 1)

    plt.plot(range(1, sim + 1), win)

probNrUsi(30, 10000)
plt.show()