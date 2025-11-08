import numpy as np
import matplotlib.pyplot as plt

P = np.array([1/6, 4/6, 1/6])
M_VALS = np.array([0.5, 1.05, 1.5])

def simulate_paths(S0, f, rounds=300, num_paths=10_000, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.choice(3, size=(rounds, num_paths), p=P)
    M = M_VALS[idx]
    G = (1 - f) + f * M
    W = np.empty((rounds + 1, num_paths), dtype=float)
    W[0] = S0
    W[1:] = S0 * np.cumprod(G, axis=0)
    return W

def ar_mean_path(S0, f, rounds=300):
    EG = (1 - f) + f * (P @ M_VALS)
    t = np.arange(rounds + 1)
    return t, S0 * (EG ** t)

def geo_mean_path(S0, f, rounds=300):
    g = np.sum(P * np.log((1 - f) + f * M_VALS))
    t = np.arange(rounds + 1)
    return t, S0 * np.exp(g * t)

def kelly_fraction(n=20001):
    fs = np.linspace(0.0, 1.0, n)
    g = np.array([np.sum(P * np.log((1 - f) + f * M_VALS)) for f in fs])
    i = np.argmax(g)
    return fs[i], g[i]

if __name__ == "__main__":
    S0 = 5000.0
    rounds = 300
    num_paths = 10000
    f_list = [0.25, 0.35, 0.40, 0.50, 0.60, 0.75, 1.00]
    f_paths = 0.40

    fig, ax = plt.subplots(2, figsize=(10, 7))

    for f in f_list:
        W_end = simulate_paths(S0, f, rounds=rounds, num_paths=num_paths, seed=123)[-1]
        ax[0].hist(np.log(W_end[:-1]), bins=120, alpha=0.6, density=True, label=f"{int(f*100)}%")
    ax[0].set_xlabel("log final wealth")
    ax[0].set_ylabel("density")
    ax[0].legend(title="bet fraction")

    W = simulate_paths(S0, f_paths, rounds=rounds, num_paths=num_paths, seed=42)
    t, W_ar = ar_mean_path(S0, f_paths, rounds)
    _, W_geo = geo_mean_path(S0, f_paths, rounds)
    mc_mean = W.mean(axis=1)
    mc_median = np.median(W, axis=1)
    ax[1].plot(t, np.log(mc_mean), label="MC mean")
    ax[1].plot(t, np.log(mc_median), label="MC median")
    ax[1].plot(t, np.log(W_ar), lw=2, label="Arithmetic mean (analytic)")
    ax[1].plot(t, np.log(W_geo), lw=2, label="Geometric mean (analytic)")
    ax[1].set_xlabel("round")
    ax[1].set_ylabel("log wealth")
    ax[1].legend()

    f_star, g_star = kelly_fraction()
    ax[1].set_title(f"f_paths={int(f_paths*100)}%   Kelly ≈ {f_star:.3f},  exp(E[log G]) at Kelly ≈ {np.exp(g_star):.6f}")

    plt.tight_layout()
    plt.show()
