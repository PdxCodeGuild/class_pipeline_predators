total_amount = 1.36
quarter = .25
dime = .10
penny = 0.01

quarters_results = total_amount // quarter
print(quarters_results)

quarter_change = quarters_results * quarter
print(quarter_change)

remainder_1 = total_amount - quarter_change
print(round(remainder_1, 2))


dime_results = round(remainder_1, 2) // dime
print(dime_results)

dime_change = dime_results * dime
print(dime_change)

remainder_2 = round(remainder_1, 2) - dime_change
print(round(remainder_2, 2))


penny_results = round(remainder_2, 2) // penny
print(penny_results)

penny_change = penny_results * penny
print(penny_change)

remainder_3 = round(remainder_2, 2) - penny_change
print(remainder_3)
