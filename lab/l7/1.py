import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def bernoulli(p, size):
    ev = np.random.random(size)
    return (ev < p).astype(np.int16)

def binomial(p, n, size):
    ev = np.random.random((size, n))
    return (ev < p).sum(axis = 1)

def geom(p, size):
    ev = np.random.random(size)
    return np.floor(np.log(1-ev)/np.log(1-p)) + 1

def pmf_bernoulli(k, p):
    k = np.asarray(k)
    return (k == 1)*p + (k == 0)*(1 - p)

def pmf_binomial(k, n, p): return comb(n,k).astype(np.int64) * (p**k) * ((1-p)**(n-k))
def pmf_geometric(k, p):   return (1-p)**(k-1) * p

def main():
    _, ax = plt.subplots(3, figsize=(10, 6))
    N = 10_000
    p = 0.6

    # bernoulli

    data_b = bernoulli(p, N)

    bins_b = [-0.5, 0.5, 1.5]
    ax[0].hist(data_b, bins=bins_b, density=True, label='Simulated Histogram', rwidth=0.8, align='mid')

    k_b = np.array([0.0, 1.0])
    pmf_b = pmf_bernoulli(k_b, p)
    ax[0].bar(k_b, pmf_b,
              width=0.8,
              color='none',
              edgecolor='red',
              linewidth=1.1,
              label='Theoretical PMF')
    ax[0].set_title(f'Bernoulli(p={p}) (N={N})')
    ax[0].set_xticks([0, 1])
    ax[0].set_ylabel('Probability')
    ax[0].legend()

    # binomial
    n = 30
    data_bin = binomial(p, n, N)
    bins_bin = np.arange(-0.5, n + 1.5, 1)

    ax[1].hist(data_bin, bins=bins_bin, density=True, label="Simultated Histogram", rwidth=0.8, align='mid')

    k_bin = np.arange(0, n + 1)
    pmf_bin = pmf_binomial(k_bin, n, p)


    ax[1].bar(k_bin, pmf_bin,
              width=0.8,
              color='none',
              edgecolor='red',
              linewidth=1.1,
              alpha=0.9,
              label='Theoretical PMF')
    ax[1].set_title(f'Binomial(p={p}) (k = {N}) (N={N})')
    ax[1].set_xticks([0, 1])
    ax[1].set_ylabel('Probability')
    ax[1].legend()

    # geometric

    data_g = geom(p, N)

    plot_max = int(np.max(data_g))
    plot_max = min(plot_max, 30) # cap
    geom_bin = np.arange(0.5, plot_max + 1.5, 1)

    ax[2].hist(data_g, bins=geom_bin, density=True, label="Simultated Histogram", rwidth=0.8, align='mid')

    k_geom = np.arange(1, plot_max + 2)
    pmf_geom = pmf_geometric(k_geom, p)

    ax[2].bar(k_geom, pmf_geom,
              width=0.8,
              color='none',
              edgecolor='red',
              linewidth=1.1,
              alpha=0.9,
              label='Theoretical PMF')
    ax[2].set_title(f'Geometric (p={p}) (N={N})')
    ax[2].set_xticks([0, 1])
    ax[2].set_ylabel('Probability')
    ax[2].legend()

    plt.show()
    # plt.savefig('./imgs/1.svg')


if __name__ == '__main__':
    main()