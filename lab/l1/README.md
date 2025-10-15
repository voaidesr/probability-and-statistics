# Bertrand's paradox

Bertrand's Paradox demonstrates that probabilities can depend on the method by which a random selection is made.

The paradox is centered on a single question: What is the probability that a random chord drawn in a circle is longer than the side of an inscribed equilateral triangle?

## First choice of chord

The **Random Endpoints Method**. In this simulation, two random points are chosen on the circumference and connected. Visually, about one-third of the chords are longer than the side of an inscribed equilateral triangle (shown in red).


The probability is $\frac{1}{3}$. Simulating this choice with 10'000 chords, this image is rendered:

![](./img/probability1.svg)

## Second choice of chord

The **Random Radius Method**. A chord is uniquely determined by a perpendicular to a chord. In this simulation, a random radius is chosen (by choosing a random angle $\varphi$) and a random point on the radius (by choosing a random distance on the radius $d \in [0, 1]$).

The chord length is related to this distance: $l = 2 \sqrt{1 - d^2}$. The side of the inscribed triangle is $\sqrt{3}$.

A chord is longer than the side if

$$
2 \sqrt{1 - d^2} \geq \sqrt{3} \implies d \leq \frac{1}{2}
$$

All choice of radius is symmetric, therefore the probability is $\frac{1}{2}$. Simulating this choice with 10'000 chords, this image is rendered:

![](./img/probability2.svg)
