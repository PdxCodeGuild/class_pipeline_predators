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

'''
python
coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
'''

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
    'quarters': 25, 
    'dime': 10, 
    'penny': 1
    }

# then break down amount from position in number?....
# can you index a float
# look into modulas 
#may if statement
for i in range(20):
    if i%2 == 1:
        continue
    print(i, end=' ')

# Return quarters variable and so on 

return quarters 
return dime 
return nickel 
return pennies 