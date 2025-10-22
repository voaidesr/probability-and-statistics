import numpy as np
import matplotlib.pyplot as plt

num_sim = 100000
rand = np.random.random(num_sim)
rand2 = np.random.random(num_sim)
rand3 = np.random.random(num_sim)

red =  2 * (rand < 1/2) + 5 * (rand > 1/2)
green = 3 * (rand2 < 5/6) + 6 * (rand2 > 5/6)
black = 1 * (rand3 > 5/6) + 4 * (rand3 < 5/6)

rvg = np.cumsum(red > green) / np.arange(1, num_sim + 1)
rvb = np.cumsum(red > black) / np.arange(1, num_sim + 1)
gvb = np.cumsum(green > black) / np.arange(1, num_sim + 1)

plt.plot(np.arange(1, num_sim + 1), rvg, 'r', label="red vs green")
plt.plot(np.arange(1, num_sim + 1), rvb, 'black', label="red vs black")
plt.plot(np.arange(1, num_sim + 1), gvb, 'g', label="green vs black")
plt.ylim((0.2, 0.7))
plt.legend()
plt.show()