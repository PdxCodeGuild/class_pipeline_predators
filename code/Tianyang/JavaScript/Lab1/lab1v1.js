const question = prompt("what is the distance in feet?")
const conv = {
    ft : 0.3048,
    mi : 1609.34,
    m : 1,
    km : 1000
}
const ans = question+' ft is ' +question*conv.ft+' m'
console.log(ans)