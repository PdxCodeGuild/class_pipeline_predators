user_input = float(input('Please enter an amount of money in dollars:  '))

total = user_input * 100

quarters = total // 25

total = total - quarters * 25

dimes = total // 10

total = total - dimes * 10

nickels = total // 5

total = total - nickels * 5

pennies = total // 1

total = total * pennies * 1


print(f'Your total is {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies!!')