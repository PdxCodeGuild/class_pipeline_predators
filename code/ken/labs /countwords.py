

# Lab 15: Count Words

#Grabbed the book here.
with open('countwordtext.txt', 'r', encoding='utf-8') as file:
#Turned the file into text. Text read the entire file
    text = file.read()
#Prints Text into terminal
#----print(text)-----
#I can use text to make everything lower case - variable text
text = text.lower()
#Prints new lowercase text
#------print(text)-------
#Then use the text to strip punctuaction 
#Function special strip to return new book with special characters stripped
def special_strip(text):
    for x in text:
        if x.isalpha() or x == ' ':
            continue
    else:
        text = text.replace(x,'')
    return text
#Now call the function to get the new book with special characters removed
special_strip(text)
# Splits book into seperate words
text = text.split()
#print text list.
#print(text)
#Returns list of words


#Now I need to make a dictionary of words
#Test text to test function
#text = ['yo','check','me','out','yo']


    #Define dictionary 
text_dict = {}
    #Add word to dictionary
def dict_build(text, text_dict):
    for x in text:
        if x in text_dict:
    #if x is in text dictionary then increase value by 1
            text_dict[x] +=  1
    #else add x to the dictionary with a value of 1
        else:
            text_dict[x] = 1
    return text_dict

#testing function
#print(dict_build(text, text_dict))
dict_build(text, text_dict)
#print(text_dict)

#---works----


#word_dict is a dictionary where the key is the word and the value is the count
#word_dict = {'apples': 2, 'bananas': 1, 'pears': 1, 'kiwi': 7}
words = list(text_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])






'''
Take the following steps to build up our dictionary. The result should look something like `{'a': 3, 'the': 4}`

1. 
**** DONE ****
Make everything lowercase,
**** DONE *****  
strip punctuation, 
----- inserting function from to remove special characters ------ 
***Done***
split into a list of words.
**** DONE ****
2. Your dictionary will have words as `keys` and counts as `values`. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
**** DONE ****
3. Print the most frequent top 10 out with their counts. You can do that with the code below.
'''




