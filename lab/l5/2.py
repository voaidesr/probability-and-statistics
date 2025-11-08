import numpy as np
import matplotlib.pyplot as plt

def bev(list):
    return np.exp(np.log(list).mean())

def get_list(w, alpha=0.0):
    l = np.array([1, 2, 6, 22, 200, 1e6], dtype=float)
    return l + (1 - alpha) * w * np.ones(6)

def get_kelly_pt(w):
    st = 0
    dr = 1

    while (True):
        alpha = (st + dr) / 2
        list = get_list(w, alpha)
        if bev(list) < w - 1e-7:
            dr = alpha
        elif bev(list) > w + 1e-7:
            st = alpha
        else:
            return alpha

if __name__ == '__main__':
    w = np.linspace(100, 1e5, 1000)
    k = [round(get_kelly_pt(v) * 100, 2) for v in w]
    plt.plot(w, k)
    plt.grid(True)
    plt.show()