import random
options = ['rock', 'paper', 'scissors']
print('''---------------------------
Welcome to Rock, Paper, Scissors!

Here are your options:
''')
for choice in options:
    # Capitalize first letter of each choice for print out
    choice = choice.capitalize()
    print(f'• {choice}')
play_again = 'yes'
# Loop for multiple plays
while play_again == 'yes':
    print()
    comp_choice = random.choice(options)
    player_choice = str(input('Please enter your selection: '))
    print()
    # Make sure selection is all lower case like options
    player_choice = player_choice.lower()
    # Spelling/word check
    while player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors':
        player_choice = str(input('Please check spelling and re-enter your selection: '))
        player_choice = player_choice.lower()
        print()
    if player_choice == comp_choice:
        print(f'Tie game! We both chose {comp_choice}.')
    elif player_choice == 'rock' and comp_choice == 'paper':
        print('My paper covers your rock so I win!')
    elif player_choice == 'paper' and comp_choice == 'rock':
        print('Your paper covers my rock so you win!')
    elif player_choice == 'rock' and comp_choice == 'scissors':
        print('Your rock crushes my scissors so you win!')
    elif player_choice == 'scissors' and comp_choice == 'rock':
        print('My rock crushes your scissors so I win!')
    elif player_choice == 'paper' and comp_choice == 'scissors':
        print('My scissors cut your paper so I win!')
    elif player_choice == 'scissors' and comp_choice == 'paper':
        print('Your scissors cut my paper so you win!')
    print()
    play_again = input('Would you like to play again? (yes or no) ')
print('''
OK, come back soon!
---------------------------''')