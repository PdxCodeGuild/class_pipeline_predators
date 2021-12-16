# Rot Cipher
import string
import random

letters = string.ascii_letters
user_input = 'hello world'

def rot13(user_input): 
    for i in user_input:
        if letters.index(i) < 13:
            user_input += letters([letters.index(i) + 13])
        
print(rot13)