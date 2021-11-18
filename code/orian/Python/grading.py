
while True:
    try: 
        grade_prec = float(input("Enter your grade in a number value to convert to a letter grade "))
        break
    except ValueError:
        print("Try again")
    

grade_float = float(grade_prec)
grade_int = round(grade_float)
#print(grade_int) 
grade = int(grade_int)

remainder = (grade % 10)

if remainder >= 7:
    remainder = '+'
elif remainder >= 4:
    remainder = " "
elif remainder <= 3:
    remainder = "-"

if grade > 100:
    print ('No extra credit')
elif grade == 100:
    print("A+")
elif grade >= 90:
    print(f"A{remainder}")
elif grade >= 80:
    print(f"B{remainder}")
elif grade >= 70:
    print(f"C{remainder}")
elif grade >= 60:
    print(f"D{remainder}")
elif grade < 60:
    print('F')


"""
remainder = (grade % 10)
print(remainder)

if remainder >= 7:
    print('+')
elif remainder >= 4:
    print(" ")
elif remainder <= 3:
    print("-")
  


if grade > 100:
    print ('No extra credit')
elif grade < 60:
    print('F')
elif grade > 59 and > 64:
    print("F-")

elif grade >= 97:
    print("A+")
elif grade >= 94:
    print ("A")
elif grade <= 93:
    print("A-")
elif grade <= 89:
    print("B+")
elif grade <= 86:
    print("B")
elif grade >= 60:
    print("D")
"""