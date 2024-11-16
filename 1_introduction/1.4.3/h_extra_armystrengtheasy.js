// Army Strength (Easy and Hard)

function main() {
    let numCases = parseInt(readline())
    for (let i = 0; i < numCases; i++) {
        readline(); readline()
        let gArmy = readline().split(" ").map(n => parseInt(n))
        let mArmy = readline().split(" ").map(n => parseInt(n))
        let maxGArmy = Math.max(...gArmy)
        let maxMArmy = Math.max(...mArmy)
        if (maxGArmy >= maxMArmy) {
            console.log("Godzilla")
        } else {
            console.log("MechaGodzilla")
        }
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