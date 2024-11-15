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
    return inputString[currentLine++]; // returns undefined when array overflow happens
}

// Solution

function main() {
    let line = readline()
    while (line !== undefined && line !== "") {
        let [num_1, num_2] = line.split(" ").map(n => parseInt(n))
        let ans = Math.abs(num_1 - num_2)
        console.log(ans)
        line = readline()
    }
}