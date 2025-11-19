import numpy as np
import matplotlib.pyplot as plt

def sim(n_ap=20, n_sim=10_000):
    apps = np.arange(1, n_ap+1)
    results = []

    for k in range(1, n_ap):
        cnt = 0
        for _ in range(n_sim):
            np.random.shuffle(apps)
            max = np.min(apps[:k])
            for a in apps[k:]:
                if a < max:
                    if a == 1:
                        cnt +=1
                    break
        results.append(cnt / n_sim)

    plt.plot(np.arange(1, n_ap), results)
    plt.grid()
    plt.xlabel("k (number of applicants skipped)")
    plt.ylabel("Probability of picking the best applicant")
    plt.title("Secretary problem – success rate vs. first k eliminations")
    return results

def main():
    sim(500, 10_000)
    plt.savefig('./imgs/1.svg')


if __name__ == "__main__":
    main()
