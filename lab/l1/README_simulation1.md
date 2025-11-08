# simulation1.py – Random Endpoints Method

This script draws 10,000 random chords by sampling two endpoints uniformly on the unit circle and plots them on top of the reference equilateral triangle. The proportion of red chords converges toward the analytical probability of 1/3.

![Random endpoints chords](./img/probability1.svg)

## Running the simulation

```bash
python simulation1.py
```

- Uses NumPy for the random angles and Matplotlib for rendering.
- Prints the empirical probability of drawing a chord longer than the triangle side.
- Saves the figure to `img/probability1.svg` (already generated).

Tweak `samples` to change how many chords are drawn; higher counts reduce noise but increase runtime.
