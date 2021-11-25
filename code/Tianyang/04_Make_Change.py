dollar_amount = float(input("Please enter a dollar amount(two dcimals): "))
q = int(dollar_amount*100//25)
d = int((dollar_amount*100-q*25)//10)
n = int((dollar_amount*100-q*25-d*10)//5)
p = int((dollar_amount*100-q*25-d*10-n*5)/1)
list_dict = {1:'quarter', 2:'dime', 3:'nickel', 4:'penny'}
count_dict = {1:q, 2:d ,3:n, 4:p} 
for i in range(1,5):
    while True:
        if count_dict[i] == 0:
            i =+ 1
        else:
            print(f'{count_dict[i]} {list_dict[i]},', end = ' ') 
            i =+ 1
        break
