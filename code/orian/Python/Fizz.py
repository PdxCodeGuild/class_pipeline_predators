for i in range(31):
    if i % 3 == 0 and i % 5 == 0:
        print (f' {i} fizzBuzz')
    elif i % 3 == 0:
        print (f'{i}  Fizz')
    elif i % 5 == 0:
        print ( f' {i} Buzz')
    else:
        print(i)