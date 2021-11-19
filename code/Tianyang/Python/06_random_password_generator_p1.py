import random
import string
len = int(input('Please enter the password of length: '))
i =0
while i < len:
    print(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits), end = '')
    i += 1