

total_amount = int(input('Enter a dollar amount: '))


quarters = total_amount // 25
print(f'you have {quarters} quarters')


leftover_quarters = total_amount % 25
print(leftover_quarters)

dimes_left = leftover_quarters // 10
print(f'you have {dimes_left} dimes')

leftover_dimes = dimes_left % 10
print(leftover_dimes)

nickles_left = leftover_dimes // 5
print(f'you have {nickles_left} nickles')

leftover_nickes = nickles_left % 5
print(leftover_nickes)

pennies_left = leftover_nickes // 1
print(f'you have {pennies_left} pennies')

print('thank you!')


'''
print(f'you have {quarters} quarters')   
change = float(total_amount) - float(quarters) 


if float(change) // .10:
    dimes = float(change) / .10
    print(f'you have {dimes} dimes')
change2 = float(quarters) - float(dimes)


if float(change2) / .05:
    nickles = float(change2) / .05
    print(f'you have {nickles} nickles')

'''



   