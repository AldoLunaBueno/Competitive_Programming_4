# Competitive_Programming_4

Favorites:

- 2.2 Pipe Rotation
- 2.2 Astro
. 2.2 Queens
- 2.2 Rock Band
- 2.2 Tetris
- 2.2 Add 'Em Up!

Hard unsolved problems:

- 1.6 Workout
- 2.2 Magic Sequence

Some useful snippets

```python
def solve_linear_congruence(a, b, m):
    """
    Returns the first solution of the linear congruence a x ≡ b (mod m)
    If there is no solution, returns -1
    """
    g = gcd(a, m)
    if b % g != 0:
        return -1
    else:
        a, b, m = a//g, b//g, m//g
        a_inv = pow(a, -1, m)
        return b * a_inv % m
```
