const money = { 0 : 0,
                1 : 4,
                2 : 7,
                3 : 100,
                4 : 50000,
                5 : 1000000,
                6 : 25000000
}
let stats = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

function drawNumbers() {
    const ticket = [];
    for (let count = 0; count < 6; count++)
        ticket.push(Math.floor(Math.random() * 100));
    return ticket;
}
const winner = drawNumbers();

const draws = prompt('Enter the number tickets:')

let matchCount = 0;
let totalWinnings = 0;

function checkTickets() {  
    let winCount = 0;  
    let newTicket = drawNumbers();
    // console.log(newTicket);
    for (let index = 0; index < 6; index++)
        if (winner[index] == newTicket[index])
        winCount++, matchCount++;
    stats[winCount]++;    
    totalWinnings += money[winCount];
    // return winCount;  
}

for (counter = 0; counter < draws; counter++) {
    matches = checkTickets();
    // console.log(matches); 
}
let cost = draws * 2;
console.log(`Master ticket: ${winner}`);
console.log("Stats: ",stats);
console.log(`Matches: ${matchCount}`);
console.log(`Cost: $${cost}`);  
console.log(`Winnings: $${totalWinnings}`);
console.log(`Net proceeds: $${totalWinnings - cost}`);  
