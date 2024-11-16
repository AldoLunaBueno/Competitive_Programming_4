# Competitive_Programming_4

To test any solution, you need to set the current directory there, edit the 

Favorites:

- 2.2 Pipe Rotation
- 2.2 Astro
. 2.2 Queens
- 2.2 Rock Band
- 2.2 Tetris
- 2.2 Add 'Em Up!
- 2.2 Booking
- 2.2 Join Strings
- 2.3 Juggling Patterns
- 2.3 Foppy
- 2.3 Deduplicating Files
- 2.4 Almost Union-Find

Hard unsolved problems:

- 1.6 Workout
- 2.2 Magic Sequence

Some useful snippets

Python: modular arithmetic

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

Node JS: read stadard input

``` js
function main() {
    // PUT YOUR CODE HERE
}

// Readline

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readline() {
    // returns empty string ("") if no input is given.
    // returns undefined when array overflow happens.
    return inputString[currentLine++];
}
```

In Windows we can't pass an EOF signal to the stdin (standard input)
through keyboard like a user. This is an issue with Javascript,
because it can be done in Python.
