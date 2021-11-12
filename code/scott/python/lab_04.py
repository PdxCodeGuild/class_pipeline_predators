amount = float(input('\nEnter a dollar amount: '))
pennies = amount * 100
while pennies >=1:
    print()
    if pennies >= 25:
        quarters = pennies // 25
        print(f'{int(quarters)} quarter(s)')
        pennies = (pennies % 25)
    if pennies >= 10:
        dimes = pennies // 10
        print(f'{int(dimes)} dime(s)')
        pennies = pennies % 10
    if pennies >= 5:
        nickles = (pennies // 5)
        print(f'{int(nickles)} nickel(s)')
        pennies = pennies % 5
    if pennies >= 1:
        print(f'{int(pennies)} penny(s)')
        break
print()