import numpy as np
import matplotlib.pyplot as plt

# throw = np.random.random() < 0.5

num_sim = 100000

# creeaza un np.array cu num_sim valorii bool (rezultate din compararea a n numere num_sim cu 0.5)
def vectorized(num_sim):
    tosses = np.random.random(num_sim) < 0.5
    prob = np.cumsum(tosses) / np.arange(1, num_sim+1)

    tosses2 = np.random.random(num_sim) < 1/3
    prob2 = np.cumsum(tosses2) / np.arange(1, num_sim + 1)

    # print(prob[-1])
    plt.ylim((0.2, 0.6))
    plt.plot(np.arange(1, num_sim + 1), prob, 'black')
    plt.plot(np.arange(1, num_sim + 1), prob2, 'r', label='masluita')
    plt.legend()
    plt.show()

def slow(num_sim):
    count = 0
    count2 = 0
    list = []
    list2 = []
    for k in range(1, num_sim):
        count += np.random.random() < 0.5
        list.append(count / k)
        count2 += np.random.random() < 1/3
        list2.append(count2 / k)
    plt.ylim((0.2, 0.6))
    plt.plot(np.arange(1, num_sim), list, 'black')
    plt.plot(np.arange(1, num_sim), list2, 'r', label='masluita')
    plt.legend()
    plt.show()

slow(num_sim)