total_amount = 1.36
quarter = .25
dime = .10
penny = 0.01

#factoring in quarters
quarters_results = total_amount // quarter

quarter_change = quarters_results * quarter

remainder_1 = total_amount - quarter_change


#factoring in dimes 
dime_results = round(remainder_1, 2) // dime

dime_change = dime_results * dime

remainder_2 = round(remainder_1, 2) - dime_change


#factoring remainder in pennies
penny_results = round(remainder_2, 2) // penny

penny_change = penny_results * penny

remainder_3 = round(remainder_2, 2) - penny_change


results = f' You have {quarters_results} quarters, ' + f'{dime_results} dime, and' + f' {penny_results} penny'
print(results)