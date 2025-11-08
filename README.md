# Probability & Statistics

A collection of probability-and-statistics laboratory exercises implemented in Python. Each lab lives under `lab/lX/` and focuses on a specific concept, from Bertrand's paradox to Kelly betting.

## Documentation layout
- `lab/lX/README.md` offers a general overview of the experiments inside a lab.
- `lab/lX/README_<script>.md` provides detailed instructions for each script (parameters, plots, interpretations) and embeds the pre-generated images from `lab/lX/img/`.
- The root README serves as a quick index to jump into any lab or per-script reference.

## Labs
1. **Lab 1 – Bertrand's paradox** ([overview](./lab/l1/README.md))
   - [simulation1.py](./lab/l1/README_simulation1.md): random endpoints method (P = 1/3).
   - [simulation2.py](./lab/l1/README_simulation2.md): random radius method (P = 1/2).
2. **Lab 2 – Random number generators** ([overview](./lab/l2/README.md))
   - [ex1.py](./lab/l2/README_ex1.md): law of large numbers for fair vs. biased coins.
   - [ex3.py](./lab/l2/README_ex3.md): non-transitive dice tournament.
3. **Lab 3 – Conditional probability** ([overview](./lab/l3/README.md))
   - [1.py](./lab/l3/README_1.md): posterior of supplier C given alerts.
   - [2.py](./lab/l3/README_2.md): probability of a three-head streak in 20 flips.
4. **Lab 4 – Conditional decisions** ([overview](./lab/l4/README.md))
   - [1.py](./lab/l4/README_1.md): generalised Monty Hall win rates when switching.
   - [2.py](./lab/l4/README_2.md): spam-filter precision under varying alerts.
5. **Lab 5 – Risky games and growth** ([overview](./lab/l5/README.md))
   - [1.py](./lab/l5/README_1.md): bankroll trajectories in the St. Petersburg paradox.
   - [2.py](./lab/l5/README_2.md): Kelly-optimal fraction versus bankroll.
6. **Lab 6 – Kelly growth dynamics** ([overview](./lab/l6/README.md))
   - [1.py](./lab/l6/README_1.md): wealth distributions and analytic means for fixed bet fractions.

## Reproducing figures
Most scripts can be run directly with `python <file.py>`. Each one saves its visualisation into the corresponding `img/` folder so the documentation stays in sync without modifying the underlying code.
