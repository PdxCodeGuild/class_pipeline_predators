from typing import Counter
import requests
import string
response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
a = (response.text).lower()
a = ''.join([i for i in a if i not in string.punctuation])
a = a.split()
a= Counter(a)
words = list(a.items()) 
words.sort(key=lambda tup: tup[1], reverse=True) 
for i in range(min(10, len(words))):  
    print(words[i])
