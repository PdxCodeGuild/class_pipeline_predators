import random

card_val = {
    King : 10,
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

for i in card_val:
    print(','.join(card_val))

print(i)