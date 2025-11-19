import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from discrete import discrete_variable
from vars import binomial


def poisson(l, k):
    k = np.asarray(k)
    p = (np.exp(-l) * np.power(l, k)) / factorial(k)
    p = p / p.sum()
    return p

def main():
    fig, ax = plt.subplots(3)
    N = 100_000
    l = 1

    x = np.arange(20)
    p1 = poisson(l, x)
    p2 = poisson(l + 3, x)
    p3 = poisson(l + 6, x)

    data1 = discrete_variable(x, p1, N)
    data2 = discrete_variable(x, p2, N)
    data3 = discrete_variable(x, p3, N)

    bins = np.arange(-0.5, x.max() + 1.5, 1).tolist()

    ax[0].hist(data1, bins=bins, density=True, align='mid', label=fr'$\lambda$ = {l}, N = {N}', rwidth=0.8, alpha=0.8)
    ax[1].hist(data2, bins=bins, density=True, align='mid', label=fr'$\lambda$ = {l + 3}, N = {N}', rwidth=0.8, alpha=0.8)
    ax[2].hist(data3, bins=bins, density=True, align='mid', label=fr'$\lambda$ = {l + 6}, N = {N}', rwidth=0.8, alpha=0.8)

    n = 20
    data_bin = binomial(l/n, n, N)
    ax[0].hist(data_bin, bins=bins, density=True, align='mid', label=fr'Binomial (n = {n}), (p = $\lambda$/n = {l/n}), N = {N}', rwidth=0.8, alpha=0.6)



    ax[1].bar(x, p2,
              width=0.8,
              color='none',
              edgecolor='r',
              linewidth=1.1)
    ax[2].bar(x, p3,
              width=0.8,
              color='none',
              edgecolor='r',
              linewidth=1.1)
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()
    plt.show()



if __name__ == '__main__':
    main()
