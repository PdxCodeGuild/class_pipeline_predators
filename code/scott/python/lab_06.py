char_len = int(input('\nEnter the character length for password: '))
import random
import string
options = (string.ascii_letters) + (string.digits)
password = str()
counter = 1
while counter <= char_len:
    password = password + random.choice(options)
    counter += 1
print(f'Here is your random password: {password}')
print()