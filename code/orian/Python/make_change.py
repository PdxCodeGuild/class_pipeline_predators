##$1.36 make 136 pennies 
while True:
    try: 
        amt = float(input("Enter a dollar amount to get change: "))
        break
    except ValueError:
        print("try again")

#amt = 1.36 #change later
num = round(amt * 100)
#print(num)

while amt >= 0:
        q = (num // 25)
       # print(f"{q} quarter(s)")
        d = ((num % 25) // 10) 
        #print(f"{d} dime(s)")
        tot_l = (num % 25)
        #print(tot_l)
        tot_l = (tot_l - (d * 10))
        n = tot_l // 5
       # print(f"{n} nickel(s)")
        tot_l = (tot_l - (n * 5))
        #print(tot_l)
        p = tot_l // 1
        #print(f"{p} penny(ies)")
        print(f"{q} quater(s), {d} dime(s), {n} nickel(s), {p} penny(ies)  is your coins back from ${num / 100}")
        break
  

   
