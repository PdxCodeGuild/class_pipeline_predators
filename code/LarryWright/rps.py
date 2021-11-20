# rps (Rock, Paper, Scissors)
import random

options = ["Rock", "Paper", "Scissors"]

human_choice = input(" Enter your selection (Rock, Paper, Scissors): ")

print(options)

computer_choice = random.choice(options)

if human_choice == computer_choice:
    print(" It's a Tie. ")


elif human_choice == "Rock" :
    if computer_choice == "Paper":
            print("Paper beats rock. You lose.")


elif human_choice == "Rock":
    if computer_choice == "Scissors":
        print(" Rock beats Scissors. You Win. ")


elif human_choice == "Paper" :
    if computer_choice == "Rock":
            print("Paper beats rock. You Win.")


elif human_choice == "Paper":
    if computer_choice == "Scissors":
        print(" Scissors beats Paper. You Lose. ")


elif human_choice == "Scissors":
    if computer_choice == "Rock":
             print(" Rock beats Scissors. You lose. ")

elif human_choice == "Scissors":
    if computer_choice == "Paper":
        print(" Rock beats Scissors. You Win. ")
