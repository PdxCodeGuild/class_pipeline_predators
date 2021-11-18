while True:
    try: 
        grade_prec = int(input("Enter your grade in a number value to convert to a letter grade "))
        break
    except ValueError:
        print("Try again")