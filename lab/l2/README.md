# Random number generators

## HRNG

Generate random numbers through hardware means. Very inefficent for many numbers, cannot be replicated.

## PRNG

Uses a predefined list of numbers in $[0, 1]$ and picks a random position. Can be replicated.

In numpy:

```py
np.random.seed(seed_number)
```