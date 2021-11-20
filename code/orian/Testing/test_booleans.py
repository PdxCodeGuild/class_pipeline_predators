
import pytest

# Practice 2: Booleans, Comparisons, & Conditionals
# Copy and paste this file into your own "02_booleans.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 02_booleans.py"


# Go Hiking
# Write a function that takes a string indicating energy level and weather

energy = ('tired', 'spry')
weather = ('rainy', 'sunny')
a = 'tired'
b = 'sunny'

def go_hiking(energy, weather):
    if energy == 'spry' and weather == 'sunny':
        return True
    else:
        return False

print(go_hiking(a,b))



def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True




# Double Digit
# Write a function that returns True if the number is a double digit

def double_digit(num):
    if num >= 10 and num <= 99:
        return True
    elif num >= -99 and num <= -10:
        return True 
    else:
        return False

def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True

pytest

# Opposite
# Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.

def opposite(a, b):
    if a  <= -1 and b >= 0:
        return True
    elif a  >= 0 and b <= -1:
        return True
    else:
        return False

def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False
pytest


# Near 100
# Write a function that returns True if a number within 10 of 100.


def near_100(num):
    if num >= 90 and num <= 110:
        return True
    else:
        return False

def test_near_100():
    assert near_100(50) == False
    assert near_100(99) == True
    assert near_100(105) == True
    assert near_100(115) == False


# Maximum of Three
# Write a function that returns the maximum of 3 parameters.
print(max(5,6,2))

def maximum_of_three(a, b, c):
    return (max)(a,b,c)

def test_maximum_of_three():
    assert maximum_of_three(5,6,2) == 6
    assert maximum_of_three(-4,3,10) == 10
