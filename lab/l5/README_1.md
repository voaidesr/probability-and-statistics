# 1.py – St. Petersburg Paradox Simulator

This script models repeated entries into the St. Petersburg lottery. Each game costs `price_per_game`, the prize doubles while the die keeps missing (probability `1 - p`), and the player aims to reach a target wealth or go broke.

## Running the simulator

```bash
python 1.py
```

- `wealth` is the starting bankroll; the goal is defaulted to `10 * wealth`.
- `p` is the probability of the game stopping on a given round (default `1/6`).
- Every simulation prints intermediate wealth and whether the player survived.

Because the expected payout is infinite but variance is enormous, this code is useful for visualising bankroll trajectories and estimating ruin probabilities. Consider patching in custom logging if you want plots—currently the script focuses on textual output.
