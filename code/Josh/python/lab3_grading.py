try:
    user_input = int(input('Please enter your number:  '))
except:
    user_input = int(input('Incorrect response, please put your number:  '))



if user_input >= 97 and user_input <= 100:
    print('You got an A+!')
elif user_input >= 93 and user_input <= 96:
    print('You got an A!')
elif user_input >= 90 and user_input <= 92:
    print('You got an A-!')
elif user_input >= 87 and user_input <= 89:
    print('You got an B+!')
elif user_input >= 83 and user_input <= 86:
    print('You got an B!')
elif user_input >= 80 and user_input <= 82:
    print('You got an B-!')
elif user_input >= 77 and user_input <= 79:
    print('You got an C+!')
elif user_input >= 73 and user_input <= 76:
    print('You got an C!')
elif user_input >= 70 and user_input <= 72:
    print('You got a C-!')
elif user_input >= 67 and user_input <= 69:
    print('You got a D+!')
elif user_input >= 65 and user_input <= 66:
    print('You got a D!')
elif user_input >= 0 and user_input <= 65:
    print('You got an F!')


