
num1 = 12
num2 = -3
num3 = 4

def is_divided_by(number, a, b):
    if number / a and number  / b >= 0:
        return True
    if number / a and number / b != 0:
        return False


results = is_divided_by(num1, num2, num3)

print(results)
