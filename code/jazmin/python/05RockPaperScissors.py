import random
choices = ['Rock', 'Paper', 'Scissors']

print('welcome to Rock, Paper, Scissors! \nyour options are: Rock, Paper or Scissors')

user_choice = input('please enter your selection: ')
print(f'you have selected {user_choice}')

computer_choice = random.choice(choices)
print(f'the computer selected {computer_choice}')


if user_choice.title() == 'Rock' and computer_choice.title() == 'Rock':
    print('You have tied with the computer.')

elif user_choice.title() == 'Rock' and computer_choice.title() == 'Paper':
    print('The computer won this game. Better luck next time!')

elif user_choice.title()== 'Rock' and computer_choice.title() == 'Scissors':
    print('Congratulations, you have won the game!')

elif user_choice.title()=='Paper' and computer_choice.title() == 'Rock':
    print('Congratulations! you have won the game')

elif user_choice.title() == 'Paper' and computer_choice.title() == 'Paper':
    print('You have tied with the computer.')

elif user_choice.title() == 'Paper' and computer_choice.title() == 'Scissors':
    print('The computer won this game. Better luck next time!')

elif user_choice.title() == 'Scissors' and computer_choice.title() == 'Rock':
    print('The computer has won this game. Better luck next time!')

elif user_choice.title() == 'Scissors' and computer_choice.title() == 'Paper':
    print('Congratulations! You have won the game.')

elif user_choice.title() == 'Scissors' and computer_choice.title() == 'Scissors':
    print('You have tied with the computer.')

