import string

with open('g_gatsby.txt', 'r') as book:
    content = book.read()
#print(content)
for char in content:
    content += char.strip(string.punctuation).lower()
#print(content)        
content_list = content.split()
#print(content_list)
word_dict = {}
for word in content_list:
    if word in word_dict:
        word_dict[word] += 1     
    else:
        word_dict[word] = 1
     
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])