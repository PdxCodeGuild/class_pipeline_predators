import random

r = "rock"
p = 'paper'
s = 'scissors'

rps_table = ['rock','paper','scissors'] 

while True:
    game_intro = input("Do you want to play Rock, Paper, Scissors? yes or no?:  ")
    if game_intro == "yes" or game_intro == "y":
        True
    elif game_intro == "no" or game_intro == "n":
        break
    
    while True:
        
        select = input(F"Choose between { ','.join(rps_table)}:  ")
        user_select = select.casefold()
        #print(user_select)
        comp_select = random.choice(rps_table)
        print(comp_select)

        if user_select == r and comp_select == p:
            print(f"You lose, {comp_select} beats {user_select}")
        elif user_select == r and comp_select == s:
            print(f"You win, {user_select} beats {comp_select}")
        elif user_select == p and comp_select == s:
            print(f"You lose, {comp_select} beats {user_select}")
        elif user_select == p and comp_select == s:
            print(f"You win, {user_select} beats {comp_select}")
        elif user_select == s and comp_select == r:
            print(f"You lose, {comp_select} beats {user_select}")
        elif user_select == s and comp_select == p:
            print(f"You win, {user_select} beats {comp_select}")
        elif user_select == comp_select:
            print("Draw")

        play_again = input("Do you want to play again?: ")

        if play_again == "yes":
            True
        elif play_again == "no":
            break
        
        


    '''
    while True:
        
        user_select = input(F"Choose between {rps_table}:  ")    
        comp_select = random.choice(rps_table)
        print(comp_select)

        if user_select == r and comp_select == p:
            print(f"You lose, {comp_select} beats {user_select}")
        elif user_select == r and comp_select == s:
            print(f"You win, {user_select} beats {comp_select}")
        elif user_select == p and comp_select == s:
            print(f"You lose, {comp_select} beats {user_select}")
        elif user_select == p and comp_select == s:
            print(f"You win, {user_select} beats {comp_select}")
        elif user_select == s and comp_select == r:
            print(f"You lose, {comp_select} beats {user_select}")
        elif user_select == s and comp_select == p:
            print(f"You win, {user_select} beats {comp_select}")
        elif user_select == comp_select:
            print("Draw")

    play_again = input("Do you want to play again?: ")

    if play_again == "yes":
        continue
    elif play_again == "no":
        break
'''  