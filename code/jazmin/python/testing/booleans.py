#hiking

def go_hiking(energy, weather):
    if energy == 'tired' and weather == 'rainy':
        return False
    
    elif energy == 'tired' and weather == 'sunny':
        return False

    elif energy == 'spry' and weather == 'rainy':
        return False

    elif energy == 'spry' and weather == 'sunny':
        return True
        

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True




# Double Digit

def double_digit(num):
    if num >= 10 and num <= 99:
        return True

    elif num <= 9 and num >=0:
        return False 

    elif num <= -10 and num >= -99:
        return True

    elif num >= -9 and num <= -1:
        return False

    else:
        return False 



def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True




# Opposite


def opposite(a, b):
    if a > 0 and b <= -1:
        return True

    elif a < 0 and b >= 1:
        return True

    elif a <= -1 and b <= -1:
        return False 

    elif a >= 1 and b >= 1:
        return False



def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False





# Near 100

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


#max of 3



def maximum_of_three(a, b, c):
    if a > b > c:
        return a 

    elif a < b > c:
        return b 

    elif a < b < c:
        return c

def test_maximum_of_three():
    assert maximum_of_three(5,6,2) == 6
    assert maximum_of_three(-4,3,10) == 10


#gracias :]

