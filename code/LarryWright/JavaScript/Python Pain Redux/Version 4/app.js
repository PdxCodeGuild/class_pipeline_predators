let num = prompt('Enter the distance:')
        let input_unit = prompt('Enter input units: "in, ft, yd, mi, m or km":')
        let output_unit = prompt('Enter output units: "in, ft, yd, mi, m or km":')
        let units = {
            "in" : .0254,
            "ft" : .3048,
            "yd" : .9144,
            "mi" : 1609.34,
            "m" : 1,
            "km" : 1000
        }
        meters = units[input_unit] * num
        answer = meters / units[output_unit]
        console.log(num+" "+input_unit+" is "+answer+" "+output_unit)
        alert(num+" "+input_unit+" is "+answer+" "+output_unit)