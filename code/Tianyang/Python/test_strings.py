import pytest
#1
def double_letters(word):
    new_list = []
    i = 0 
    while True:
        if i < len(list(word)):
            new_list.append(list(word)[i]*2)
            i += 1
        else:
            break
    return ''.join(new_list)
def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# #2
def count_letter(letter, word):
    return list(word).count(letter)

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter(
        'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


#3
def latest_letter(word):
    return str(sorted(list(word))[-1])

def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'

#4
def count_hi(text):
    return list(text).count('hi')

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2

#5 Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).
import re
def snake_case(text):
    a = text.replace(' ', '_').lower()
    return re.sub('\W', '', a)
# def test_snake_case():
#     assert snake_case('Hello World!') == 'hello_world'
#     assert snake_case('This is another example.') == 'this_is_another_example'


#6
import re
def camel_case(text):
    a = re.split('\s', text)
    b = "".join(word[0].upper() + word[1:].lower() for word in a)
    c = b[0].lower() + b[1:]
    return re.sub('\W', '', c)
def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'


#7
def alternating_case(text):
    a = ''
    for i in range(len(text)):
        if i % 2 == 0:
            a = a + text[i].upper()
        else:
            a = a + text[i].lower()
    return a

def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'