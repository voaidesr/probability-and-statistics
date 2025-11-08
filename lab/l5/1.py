import numpy as np
import matplotlib.pyplot as plt

def petersburg_paradox(wealth=100, p=1/6, price_per_game=64):
    desired_wealth = 10 * wealth
    while wealth < desired_wealth:
        wealth -= price_per_game
        prize = 1
        while np.random.random() > 1/6:
            prize *= 2
        wealth += prize

        if wealth <= 0:
            print(f"Ran out of money!")
            return False

        print(f"Current wealth: {wealth}\r\r")

    return True

def sim(ns, wealth=100, p=1/6, price_per_game=64):
    won = 0
    for i in range(ns):
        print(f" GAME {i} ".center(21, '-'))
        won += petersburg_paradox(wealth, p, price_per_game)
    print(21 * "-")
    return won / (ns + 1)

if __name__ == '__main__':
    ns = 10000
    print(f"Winning chance: {round(sim(ns, wealth=6400) * 100, 5)}%")