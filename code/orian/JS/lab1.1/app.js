const measurements={
    feet: .3048,
    meter: 3.28084,
}
let lengthmf= prompt("How many meters do you want converted to feet?")
let lengthfm= prompt("How many feet do you want converted to meters?")
mf=lengthmf
fm=lengthfm

ans1=(measurements.meter *= lengthmf)
ans2=(measurements.feet *= lengthfm)

meters=(mf + " meters equals " + ans1 + " feet")
feet=(fm + " feet equals " + ans2 + " meters")
console.log(meters,feet)

