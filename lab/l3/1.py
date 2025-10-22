import matplotlib.pyplot as plt
import numpy as np

ns = 100

def sim_unvectorised(ns):
    count = 0
    count_AC = 0
    for _ in range(ns):
        c = np.random.random() < 0.75
        if c:
            a = np.random.random() < 0.05
            count += a
        else:
            a = np.random.random() < 0.98
            count += a
        count_AC += a and c
    return count_AC/count

def sim_vectorised(ns):
    bugs = np.random.random(ns) < 0.75
    fp = (np.random.random(ns) < 0.05) & bugs
    tp = (np.random.random(ns) < 0.98) & (~bugs)

    total = np.cumsum(fp) + np.cumsum(tp)

    count = np.cumsum(bugs & fp)

    plt.plot(np.arange(1, ns + 1), count/total)
    plt.ylim(0.12, 0.14)

sim_vectorised(1000000)
plt.show()