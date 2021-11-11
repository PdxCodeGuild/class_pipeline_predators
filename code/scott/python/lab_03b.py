print()
score = int(input('Please enter your test score (0-100): '))
if score <= 59:
    print('Your letter grade is F')
else:
    if score >= 90:
        grade = 'A'
    elif score >= 80 and score <= 89:
        grade = 'B'
    elif score >= 70 and score <= 79:
        grade = 'C'
    else:
        grade = 'D'
    score_2 = score % 10
    if score_2 >=7:
        grade_2 = '+'
    elif score_2 >= 4 and score_2 <= 6:
        grade_2 = ''
    else:
        grade_2 = '-'
    print(f'Your letter grade is {grade}{grade_2}')
print()