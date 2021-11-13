total_amount = 1.36
quarter = .25
dime = .10
penny = 0.01

penny_results = total_amount // penny
dime_results = total_amount // dime
quarters_results = total_amount // quarter


print(quarters_results)

quarter_change = quarters_results * quarter

remainder_1 = total_amount - quarter_change 
print(remainder_1)



