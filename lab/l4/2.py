import numpy as np
import matplotlib.pyplot as plt

def sim_np(ns):
    spam = np.random.random(ns) < 0.3
    tp = (np.random.random(ns) < 0.8) & spam
    fp = (np.random.random(ns) < 0.05) & (~spam)

    total = np.cumsum(tp) + np.cumsum(fp)
    count = np.cumsum(tp)

    plt.plot(np.arange(1, ns + 1), count / total)

sim_np(100000)
plt.ylim(0.87 - 0.2, 0.87 + 0.2)
plt.show()
