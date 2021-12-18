import pytest

# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled

def double_numbers(nums):
    new_list = []
    for num in nums:
        new_list.append(num**2)
    return new_list

def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]


# Stars
# Write a function that takes an integer and returns that number of asterisks in a string
print(5 * "*")
def stars(n):
    star_list = []
    for ns in n:
        star_list.append(ns * "*")
def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'


# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    num_list = []
    for num in nums:
        if num  10:
            num_list.append(num)

numbers = [2,4,6,21,15,13]
numbers_1 = extract_less_than_ten(numbers)
print(numbers_1)

def test_extract_less_than_ten():
    assert extract_less_than_ten([2, 8, 12, 18]) == [2, 8]
