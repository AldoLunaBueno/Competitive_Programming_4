// Provinces and Gold

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


// Solution

/*
Province (costs 8, worth 6 victory points)    
Duchy (costs 5, worth 3 victory points)
Estate (costs 2, worth 1 victory point)

Gold (costs 6, worth 3 buying power)
Silver (costs 3, worth 2 buying power)
Cooper (costs 0, worth 1 buying power)
*/

function main() {
    let accValue = 0
    let bestVictory = null
    let bestTreasure = null

    let victoryCosts = [8, 5, 2]
    // let victoryValues = [6, 3, 1]
    let treasureCosts = [6, 3, 0]
    let treasureValues = [3, 2, 1]
    let initialTreasures = readline().split(" ").map(n => parseInt(n))
    for (let i = 0; i < 3; i++) {
        accValue += initialTreasures[i] * treasureValues[i]
    }

    // best victory card
    if (accValue >= victoryCosts[0]) {
        bestVictory = "Province"
    } else if (accValue >= victoryCosts[1]) {
        bestVictory = "Duchy"
    } else if (accValue >= victoryCosts[2]) {
        bestVictory = "Estate"
    }

    // best treasure card
    if (accValue >= treasureCosts[0]) {
        bestTreasure = "Gold"
    } else if (accValue >= treasureCosts[1]) {
        bestTreasure = "Silver"
    } else if (accValue >= treasureCosts[2]) {
        bestTreasure = "Copper"
    }

    if (bestVictory === null) {
        console.log(bestTreasure)
        return
    }
    console.log(bestVictory + " or " + bestTreasure)
}
