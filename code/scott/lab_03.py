print()
score = int(input('Please enter your test score (0-100): '))
if score >= 90:
    grade = 'A'
elif score >= 80 and score <= 89:
    grade = 'B'
elif score >= 70 and score <= 79:
    grade = 'C'
elif score >= 60 and score <= 69:
    grade = 'D'
else:
    grade = 'F'
print(f'Your letter grade is {grade}')
print()