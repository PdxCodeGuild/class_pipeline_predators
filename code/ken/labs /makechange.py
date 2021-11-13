# # Make Change

    # Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. First convert the dollar amount (1.36) into the total number of pennies (136), then use floor division `//`, which throws away the remainder. `10/3` is `3.333333`, `10//3` is `3`. 


    # ```
    # Enter a dollar amount: 1.36
    # 5 quarters, 1 dime, and 1 penny
    # ```
    # ```
    # Enter a dollar amount: 0.67
    # 2 quarters, 1 dime, 1 nickel, 2 pennies
    # ```

    # ## Version 2 (optional)

    # Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.

    # '''
    # python
    # coins = [
    #     ('half-dollar', 50),
    #     ('quarter', 25),
    #     ('dime', 10),
    #     ('nickel', 5),
    #     ('penny', 1)
    # ]
    # '''

# then use a try exception to make sure they enter a float 
while True:
    try:
        dollar_amount = float(input('enter a dollar amount: '))
        break
    except ValueError:
        print('try again')
print(dollar_amount)

# Make a dictionary for coins 
coins  = {
    'quarters': .25, 
    'dime': .10,
    'nickels': .05,
    'penny': .01
    }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

change_quarters = dollar_amount // coins['quarters']
print(change_quarters)
remainder_quarters = dollar_amount - (change_quarters * coins['quarters']) 
print(remainder_quarters) 
change_dimes = remainder_quarters // coins['dime']
print(change_dimes)
remainder_dimes = dollar_amount - ((change_quarters * coins['quarters']) + (change_dimes * coins['dime']))
print(remainder_dimes)


# print(f'{change_quarters} + quarters + {change_dimes} + dimes + {change_nickels} + pennies + {change_pennies} pennies')

# We have a float
# in order to get the change we will divide by quarters first 

change = 0 























# control = 0

# for money_point in dollar_amount:

    #    if money_point.isnumeric() == False : 
    #        continue 
    #    elif money_point.isnumeric() == True:
        
    # print(money_point)


# while control < c
    # then break down amount from position in number?....
    # can you index a float
    # look into modulas 
    #may if statement
    # for i in range(20):
    #     if i%2 == 1:
    #         continue
    #     print(i, end=' ')

    # Return quarters variable and so on 
    # You can index a list 
    # return quarters 
    # return dime 
    # return nickel 
    # return pennies 

    # Make it a list 