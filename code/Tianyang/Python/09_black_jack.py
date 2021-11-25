card ={'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'J':10, 'Q':10, 'K':10}
first_card = input("What's your first card? ")
second_card = input("What's your second card? ")
third_card = input("What's your third card? ")
def value(cards):
    for k, v in card.items():
        if cards == k:
            return v
total = value(first_card) + value(second_card) + value(third_card)     
if total < 17:
    print(f'{total} Hit')
elif 17 <= total < 21:
    print(f'{total} Stay')
elif total == 21:
    print(f'{total} Blackjack!')
elif total > 21:
    print('Already Busted')
