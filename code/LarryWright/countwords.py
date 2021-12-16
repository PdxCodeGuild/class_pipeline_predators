# Count words (Dictionary)
import string
import random

filename = 'document.txt'
lines = [line.lower() for line in filename]

with open('document.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    words = text.split()
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in words]
    print(stripped)
 