// ABC - Kattis

function main() {
    let output = []
    let abc_values = readline().split(" ").map(n => parseInt(n))
    abc_values.sort((n,m) => n - m)
    abc_positions = {"A": 0, "B": 1, "C": 2}
    abc_chars = readline()
    for (char of abc_chars) {
        let i = abc_positions[char]
        output.push(abc_values[i])
    }
    console.log(output.join(" "))
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