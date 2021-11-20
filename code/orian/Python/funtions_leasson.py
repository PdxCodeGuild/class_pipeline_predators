import random
import pytest



def say_hello(a,b):
    print(f'Hello {a} {b}.  ')

first_name = "Orian"
last_name = "Steen"

x =3
y = 5

print(say_hello(first_name, last_name))

blackjack_card = {
    "King" : 10,
    'Queen' : 10
}

card_1 = random.choice(blackjack_card.keys())
print(card_1) 
def a_functions():
    return blackjack_card.keys(), blackjack_card.values()

print(a_functions())