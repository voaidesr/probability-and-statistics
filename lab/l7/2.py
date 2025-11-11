import numpy as np
import matplotlib.pyplot as plt

def discrete_variable(vals, probs, size):
    pb_sum = np.cumsum(probs)
    r_val = np.random.random(size)
    indices = np.searchsorted(pb_sum, r_val)
    return vals[indices]

def main():
    N = 10000
    x = np.array([1, 2, 3, 4])
    p = np.array([0.1, 0.1, 0.2, 0.6])

    sim_data = discrete_variable(x, p, N)
    bins = np.arange(0.5, x.max() + 1.5, 1).tolist()

    plt.hist(sim_data, bins=bins, density=True, align='mid', rwidth=0.8)
    plt.show()

if __name__ == '__main__':
    main()