const q1 = prompt("what is the distance?")
const q2= prompt("what are the units?")
const conv = {
    ft : 0.3048,
    mi : 1609.34,
    m : 1,
    km : 1000
}
let ans = q1 + ' '+q2 + ' is ' +q1*conv[q2] +' m'
console.log(ans)