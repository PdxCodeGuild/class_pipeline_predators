#1
import pytest
def go_hiking(energy, weather):
    if energy == "spry" and weather == "sunny":
        return True
    else:
        return False


def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True

#2
import pytest
def double_digit(num):
    if int(num) > 10 and int(num) < 100:
        return True
    elif int(num) > -100 and int(num) < -10:
        return True
    else: 
        return False

def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True

#3
import pytest
def opposite(a, b):
    if a > b:
        return True
    else:
        return False

def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False

#4
import pytest
def near_100(num):
    if 90 < num < 110:
        return True
    else: 
        return False

def test_near_100():
    assert near_100(50) == False
    assert near_100(99) == True
    assert near_100(105) == True
    assert near_100(115) == False
#5
import pytest
def maximum_of_three(a, b, c):
    if a != b and b != c and a > b >= c or a > c >= b:
        return a
    elif a == b > c:
        return a or b
    elif a != b and b != c and b > a >= c or b > c >= a:
        return b
    elif a == c > b:
        return a or c
    elif a != b and b != c and c > a >= b or c > b >= a:
        return c
    elif b == c > a:
        return b or c
    elif a == b == c:
        return a or b or c
   
def test_maximum_of_three():
    assert maximum_of_three(5,6,2) == 6
    assert maximum_of_three(-4,3,10) == 10