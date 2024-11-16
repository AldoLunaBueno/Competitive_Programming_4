// Statistics

function main() {
    let line = readline()
    let i = 1
    while (line !== undefined) {
        let [_, ...data] = line.split(" ").map(n => parseInt(n))
        let min = Math.min(...data)
        let max = Math.max(...data)
        let range = max - min
        console.log(`Case ${i}: ${min} ${max} ${range}`)
        line = readline()
        i++
    }
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