import random
while True:
    user = input('Please enter you choice (rock, paper, scissors): ')
    com_list = ["rock", "paper", "scissors"]
    computer = random.choice(com_list)
    if user == computer: 
        print(f'computer pick {computer}, tie') 
    elif user == "rock":
        if computer == "scissors":
            print(f'computer picks {computer}, you win!')
        elif computer == "paper": 
            print(f'computer picks {computer}, you lose.')
    elif user == "paper":
        if computer == "rock": 
            print(f'computer picks {computer}, you win!')
        elif computer == "scissors":
            print(f'computer picks {computer}, you lose.')
    elif user == "scissors":
        if computer == "paper":
            print(f'computer picks {computer}, you win!')
        elif computer == "rock":
            print(f'computer picks {computer}, you lose.')
    answer = input("Would you like to play again? 'y' or 'n': ")
    if answer == 'n':
        break
    



