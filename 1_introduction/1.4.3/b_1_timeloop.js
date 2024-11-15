
// Header to read lines from stdin

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
    return inputString[currentLine++];
}


// Solution

function main() {
    let n = parseInt(readline())
    for (let i = 1; i <= n; i++) {
        console.log("" + i + " Abracadabra")
    }
}
