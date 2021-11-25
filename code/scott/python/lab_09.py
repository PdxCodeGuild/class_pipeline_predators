card_deck = {'a': 1, 'k': 10, 'q': 10, 'j': 10, '10': 10, '9': 9,
'8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
card_1 = input('\nEnter your first card: ')
card_2 = input('\nEnter your second card: ')
card_3 = input('\nEnter your third card: ')

def blackjack(c1, c2, c3):
    card_total = (card_deck[card_1] + card_deck[card_2] + card_deck[card_3])
    if  card_total == 21:
        print(f'\n{card_total} Blackjack!')
    elif card_total > 21:
        print(f'\n{card_total} Bust!')
    elif card_total < 21 and card_total >= 17:
        print(f'\n{card_total} Stay')
    else:
        print(f'\n{card_total} Hit')

blackjack(card_1, card_2, card_3)