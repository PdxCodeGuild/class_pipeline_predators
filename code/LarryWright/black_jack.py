import random

# make card dictionary 

card_deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

dealer_hand = []

player_hand = []


# Dealer hand #
while len(dealer_hand) != 2:
    dealer_hand.append(random.randint(1, 11))
    if len(dealer_hand) == 2:
        print( "Dealers has: ", dealer_hand)

# Player hand #
while len(player_hand) != 2:
    player_hand.append(random.randint(1, 11))
    if len(player_hand) == 2:
        print( "Your hand is: ", player_hand)

# Results
if sum(dealer_hand) == 21:
    print("Dealer Wins!")
elif sum(dealer_hand) > 21:
    print("Dealer is over!")

while sum(player_hand) < 21:
    choice = str(input("Do you want to hit or stay? "))
    if choice == "hit":
        player_hand.append(random.randint(1, 11))
        print("Your hand is now" +  str(sum(player_hand)) + " with ", player_hand)
    if choice == "stay":
        print("The dealers hand is "  + str(sum(dealer_hand)) +  " with ", dealer_hand)
        print("Your hand is " + str(sum(player_hand)) + " with ", player_hand)
        if sum(dealer_hand) > sum(player_hand):
            print("Dealer Wins!")
        else:
            print("Player wins!")
        break

if sum(player_hand) > 21:
    print("Player over, Dealer Wins!")
elif sum(player_hand) == 21:
    print("Balckjack! You win!")