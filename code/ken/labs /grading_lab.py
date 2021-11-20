
# Grading

## Part 1
'''
Let's convert a number grade to a letter grade, using `if` and `elif` statements and comparisons. First have the user enter a number representing the grade (0-100). Then convert the number grade to a letter grade.

Concepts Covered:
- `fundamentals`, `comparisons & conditionals`

Numeric Ranges:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- 0-59: F


## Part 2

Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using `if` statements, or use modulus `%` to get the ones-digit to set another string to `'+'`, `'-'`, or `' '`. Then you can concatenate that string with your grade string. 
'''

while True:
    try:
        x = int(input('enter a number: '))
        break
    except ValueError:
        print('try again')
print(x)

grade = x

if grade < 60:
    print('ya got a F')
elif grade < 65:
    print('ya got a D-')
elif grade < 7:
    print('ya got a D')
elif grade < 70:
    print('ya got a D+')
elif grade < 75:
    print('ya got a C-')
elif grade < 77:
    print('ya got a C')
elif grade < 80:
    print('ya got a C+')
elif grade < 85:
    print('ya got a B-')
elif grade < 87:
    print('ya got a B')
elif grade < 90:
    print('ya got a B+')
elif grade < 95:
    print('ya got a A-')
elif grade < 97:
    print('ya got a A')
else:
    print("ya got an A+")
