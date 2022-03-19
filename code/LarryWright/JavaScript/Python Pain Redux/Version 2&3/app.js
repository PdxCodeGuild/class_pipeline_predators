let unit = prompt('Enter the units: "ft, mi, m or km":')
        let num = prompt('Enter the number to convert to meters:')
        let units = {
            "in" : .0254,
            "ft" : .3048,
            "yd" : .9144,
            "mi" : 1609.34,
            "m" : 1,
            "km" : 1000
        }
        answer = units[unit] * num
        console.log(num + " " + unit +" is " + answer + "in" + units)
        alert(num + " " + unit +" is " + answer + " in"+ units)