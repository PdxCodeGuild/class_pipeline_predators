again = 'y'
<<<<<<< HEAD
print('\nLets find out if one integer is divisible by two others.')
=======
print('Lets find out it one integer is divisible by two others.')
>>>>>>> 5de55272b6c7c93074b9f1d0cff8d0138430c336
while again == 'y':
    numerator = int(input('\nEnter the numerator: '))
    denom_1 = int(input('Enter the first denominator: '))
    denom_2 = int(input('Enter the second denominator: '))

    def is_divide_by(num, den1, den2):
        check = numerator % denom_1 == 0 and numerator % denom_2 == 0
        
        if check == True:
            print(f'\nYes, {numerator} is divisible by {denom_1} and {denom_2}.')
        else:
<<<<<<< HEAD
            print(f'\nSorry, {numerator} is not divisible by {denom_1} and {denom_2}.')

    is_divide_by(numerator, denom_1, denom_2)

    again = str(input('\n"y" to continue or "n" to quit: '))
=======
            print(f'\nSorry, {numerator}is not divisible by {denom_1} and {denom_2}.')

    is_divide_by(numerator, denom_1, denom_2)

    again = str(input('\n"y" to continue or "n" to quit.'))
>>>>>>> 5de55272b6c7c93074b9f1d0cff8d0138430c336
    if again == 'n':
        break
