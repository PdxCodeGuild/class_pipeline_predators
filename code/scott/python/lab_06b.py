import random
import string
char_upper = int(input('\nEnter the number of uppercase letters :'))
char_lower = int(input('\nEnter the number of lowercase letters :'))
char_num = int(input('\nEnter the number of digits :'))
char_spec = int(input('\nEnter the number of special characters :'))
password = str()
opt_upper = (string.ascii_uppercase)
opt_lower = (string.ascii_lowercase)
opt_num = (string.digits)
opt_spec = (string.punctuation)
if char_upper > 0:
    counter = 1
    while counter <= char_upper:
        password = password + random.choice(opt_upper)
        counter += 1
if char_lower > 0:
    counter = 1
    while counter <= char_lower:
        password = password + random.choice(opt_lower)
        counter += 1
if char_num > 0:
    counter = 1
    while counter <= char_num:
        password = password + random.choice(opt_num)
        counter += 1
if char_spec > 0:
    counter = 1
    while counter <= char_spec:
        password = password + random.choice(opt_spec)
        counter += 1
password_list = (list(password))
random.shuffle(password_list)
password = ''.join(password_list)
print(f'\nHere is your random password: {password}')
print()