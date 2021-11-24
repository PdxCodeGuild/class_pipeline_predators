user_input1 = input('Welcome to Blackjack! \n\nenter your first card: ')
user_input2 = input('Enter your second card:  ')
user_input3 = input('Enter your third card:  ')

blackjack = {
'A': 11,
'K': 10,
'Q': 10,
'J': 10,
'10': 10,
'9': 9,
'8': 8,
'7': 7,
'6': 6,
'5': 5,
'4': 4,
'3': 3,
'2': 2,
 }

user_input1 = blackjack[user_input1]
user_input2 = blackjack[user_input2]
user_input3 = blackjack[user_input3]

total_score = user_input1 + user_input2 + user_input3

print(f'\n{total_score}\n')

if total_score == 21:
    print('Blackjack!')
elif total_score >=17 and total_score <=20:
    print('Stay!')
elif total_score < 17:
    print('Hit!')
elif total_score > 21:
    print('\n Already Busted!')