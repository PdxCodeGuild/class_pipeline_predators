# Count words (Dictionary)
import string
import random

filename = 'document.txt'

with open('document.txt', 'r', encoding='utf-8') as file:
#variable for text file  
    text = file.read()

#split text file into a string list
    words = text.split()

# remove punctuation from document text
    table = str.maketrans("", "", string.punctuation)
    count = 0
    stripped = [w.translate(table) for w in words]

# setting a value for each row
for i in stripped:
    print(i)
    count += 1
#  print results 
print(count)
