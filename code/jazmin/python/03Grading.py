score = input('please enter your score: ')

print(f'your score is {score}')

if int(score) >= 97 and int(score) <= 100 :
     print(' your grade is A+')

elif int(score) >= 93 and int(score) <= 96:
    print('your grade is A ')

elif int(score) >= 90 and int(score) <= 92:
    print('your grade is A-')

elif int(score) >= 87 and int(score) <= 89 :
    print('your grade is B+')

elif int(score) >= 83 and int(score) <= 86 :
    print('your grade is B')
    
elif int(score) >= 80 and int(score) <= 82 :
    print('your grade is B -')

elif int(score) >= 77 and int(score) <= 79 :
    print('your grade letter is C+')

elif int(score) >= 73 and int(score) <= 76 :
    print('your grade letter is C')

elif int(score) >= 70 and int(score) <= 72 :
    print('your grade letter is C-')

elif int(score) >= 67 and int(score) <= 69 :
    print('your letter grade is D+')

elif int(score) >= 65 and int(score) <= 66 :
    print('your letter grade is D')

elif int(score) >= 60 and int(score) <= 69 :
    print('your letter grade is D-')

elif int(score) >= 0 and int(score) <= 59 :
    print('your letter grade is F')

else: 
    print('entry invalid, please re-enter your score')
