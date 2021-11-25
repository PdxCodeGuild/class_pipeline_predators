import random
from typing import ValuesView

card_val = {
    'King' : 10,
    'Queen' : 10,
    'Jack'  : 10,
    'Ten'   : 10,
    'Nine'  : 9,
    'Eight' : 8,
    "Seven" : 7,
    'Six' : 6,
    'Five' : 5,
    'Four' : 4,
    'Three' : 3,
    'Two'   : 2,
    'Ace' : 1,
}
card_1 = random.choice(list(card_val.values()))
card_2 = random.choice(list(card_val.values()))
card_v = (card_1+card_2)
print(card_1, card_2)
print(card_1 + card_2)
print(card_v)

for i in range(1):
    if card_1 + card_2 == 21:
        print('Blackjack!')
    if card_1 + card_2 >= 17:
        print("stand")
    elif card_1 + card_2 < 17:
        print("hit")
bbhs = input('Would you like a hit? ')
if bbhs == "yes":
    card_3 = random.choice(list(card_val.values()))
    print(card_3)
    card_v2 = (card_3 + card_v)

for i in range(1):
    if card_3 + card_v > 21:
        print(f"{card_v2} bust")
    elif card_v + card_3 == 21:
        print(f'{card_v2} Blackjack!')
    elif card_v + card_3 >= 17:
        print(f'{card_v2} stand')
    elif card_v + card_3 < 17:
        print(f'{card_v2} hit')
bbhs = input('Would you like a hit? ')
if bbhs == "yes":
    card_4 = random.choice(list(card_val.values()))
card_v3 = card_v2 + card_4

for i in range(1):
    if card_4 + card_v2 > 21:
        print(f"{card_v3} bust")
    elif card_v2 + card_4 == 21:
        print(f'{card_v3} Blackjack!')
    elif card_v2 + card_4 >= 17:
        print(f'{card_v3} stand')
    elif card_v2 + card_4 < 17:
        print(f'{card_v3} hit')
    
if bbhs == "yes":
    card_4 = random.choice(list(card_val.values()))
card_v3 = card_v2 + card_4

for i in range(1):
    if card_4 + card_v2 > 21:
        print(f"{card_v3} bust")
    elif card_v2 + card_4 == 21:
        print(f'{card_v3} Blackjack!')
    elif card_v2 + card_4 >= 17:
        print(f'{card_v3} stand')
    elif card_v2 + card_4 < 17:
        print(f'{card_v3} hit')