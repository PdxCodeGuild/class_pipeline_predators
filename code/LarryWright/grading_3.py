# grading

number = input(' Enter a grade: ')

number = int(number)


if number >= 90:
    print("Your grade is an A")

elif number >= 80:
    print("Your grade is a B")

elif number >= 70:
    print("Your grade is a C")

elif number >= 60:
    print("Your grade is a D")

else:
    print("Your grade is an F")

#exception 
if number in range (70, 100):
    print("You passed!")

Exception
if number in range(0, 69):
    print("You Failed")

print(number)