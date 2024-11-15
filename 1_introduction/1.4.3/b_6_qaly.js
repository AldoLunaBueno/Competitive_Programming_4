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

function main() {
    let n = parseInt(readline())
    let acc_qaly = 0
    for (let i = 0; i < n; i++) {
        let [a, b] = readline().split(" ").map(x => parseFloat(x))
        acc_qaly += a*b
    }
    let ans = acc_qaly.toFixed(3)
    console.log(ans)
}