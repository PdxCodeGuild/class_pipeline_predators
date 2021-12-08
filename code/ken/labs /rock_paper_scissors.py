# Rock Paper Scissors
import random

print('Rock Paper Scissors')
# 1. The computer will ask the user for their choice (rock, paper, scissors)
user_put = input('rock, paper or scissors: ')
# 2. The computer will randomly choose rock, paper or scissors
#comp_put = 'rock'
comp_options = ['rock', 'paper', 'scissors']
comp_put = random.choice(comp_options)    
print(comp_put)

# 3. Determine who won and tell the user

# Let's list all the cases:
# - rock vs rock (tie)
# - paper vs paper (tie)
# - scissors vs scissors (tie)
if user_put == comp_put:
    print('Its a tie')
# - rock vs paper
elif (user_put == 'rock') & (comp_put == 'paper'):
    print('You lost')
# - rock vs scissors
elif (user_put == 'rock') & (comp_put == 'scissors'):
    print('You won')
# - paper vs rock
elif (user_put == 'paper') & (comp_put == 'rock'):
    print('You won')
# - paper vs scissors
elif (user_put == 'paper') & (comp_put == 'scissors'):
    print('You lost')
# - scissors vs rock
elif (user_put == 'scissors') & (comp_put == 'rock'):
    print('You lost')
# - scissors vs paper
elif (user_put == 'scissors') & (comp_put == 'paper'):
    print('You won')
    
print('Thanks for playing') 

