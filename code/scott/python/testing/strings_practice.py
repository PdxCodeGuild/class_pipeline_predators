

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
    word = ("-").join(list(text)).upper()
    return word


def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text(
        'this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'


# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    new_word = ''
    for letter in word:
        new_word += letter * 2
    return new_word


def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string


def count_letter(letter, word):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter(
        'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    letter_list = list(word)
    letter_list.sort()
    last_letter = letter_list[-1]
    return last_letter


def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    h = False
    counter = 0
    for char in text:
        if h == True and char == 'i':
            counter +=1
            h = False
        elif char == 'h':
            h = True
    return counter

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):
    special_char = ('!', '@', '#' '$', '%', '&', '*', '?', '.', ',', '/')
    new_text = text.replace(' ', '_').lower()
    for char in new_text:
        if char in special_char:
            new_text = new_text.replace(char, '')
    
    return new_text
    


def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).


def camel_case(text):
    special_char = ('!', '@', '#' '$', '%', '&', '*', '?', '.', ',', '/')
    new_text = text.title().replace(' ', '')
    for char in new_text:
        if char in special_char:
            new_text = new_text.replace(char, '')
        new_text = new_text[0].lower() + new_text[1:]
    return new_text


def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

# Alternating Case
# Write a function that converts text to alternating case.


def alternating_case(text):
    cap = True
    new_text = ''
    for char in text:
        if cap == True:
            new_text = new_text + char.upper()
            cap = False
        else:
            new_text = new_text + char.lower()
            cap = True
    return new_text

def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case(
        'This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'
