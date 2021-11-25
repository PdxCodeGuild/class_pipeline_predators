
import string
import random

digits = list(string.digits +string.punctuation + string.ascii_letters)
length = int(input("How many characters in password? "))
password ='' .join(random.choice(digits) for x in range(length))
print(password)
