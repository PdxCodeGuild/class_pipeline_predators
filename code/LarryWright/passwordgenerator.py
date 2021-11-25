
# Password Generator Lab #

import string
import random

letters = string.ascii_letters
digits = string.digits
puncuation = string.punctuation

n = letters + digits + puncuation

n = []
while len(n) < 10:
    n.append(random.choices(n))

print(n)