import string
import random


i = 1
password = []

while i < 11:

    i += 1
    password.append(random.choice(string.ascii_letters))
   
    print(password)
    


