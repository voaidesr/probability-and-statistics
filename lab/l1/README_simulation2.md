# simulation2.py – Random Radius Method

Instead of picking two endpoints, this variant samples a random radius and a random point along it to define a chord perpendicular to that radius. Highlighted chords (red) are longer than the side of the inscribed equilateral triangle; this construction converges toward probability 1/2.

![Random radius chords](./img/probability2.svg)

## Running the simulation

```bash
python simulation2.py
```

- Draws 10,000 random chords defined by `(\varphi, d)` pairs.
- Reports the fraction of chords exceeding the triangle side.
- Saves the figure to `img/probability2.svg`.

Adjust `samples` or styling constants to explore more paths; no code changes are required for documentation.
