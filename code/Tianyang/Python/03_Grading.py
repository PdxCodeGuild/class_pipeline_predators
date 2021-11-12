# enter_score = int(input('Please enter your score: '))
# if enter_score < 60:
#     print('F')
# elif enter_score < 70:
#     print('D')
# elif enter_score < 80:
#     print('C')
# elif enter_score < 90:
#     print('B')
# elif enter_score <= 100:
#     print('A')

enter_score = int(input('Please enter your score: '))
if enter_score < 60:
    print('F')
elif enter_score < 70 and 0 <= (enter_score % 10) <= 3:
    print('D-')
elif enter_score < 70 and 3 < (enter_score % 10) <= 6:
    print('D')
elif enter_score < 70 and 6 < (enter_score % 10) <= 9:
    print('D+')
elif enter_score < 80 and 0 <= (enter_score % 10) <= 3:
    print('C-')
elif enter_score < 80 and 3 < (enter_score % 10) <= 6:
    print('C')
elif enter_score < 80 and 6 < (enter_score % 10) <= 9:
    print('C+')
elif enter_score < 90 and 0 <= (enter_score % 10) <= 3:
    print('B-')
elif enter_score < 90 and 3 < (enter_score % 10) <= 6:
    print('B')
elif enter_score < 90 and 6 < (enter_score % 10) <= 9:
    print('B+')
elif enter_score < 100 and 0 <= (enter_score % 10) <= 3:
    print('A-')
elif enter_score < 100 and 3 < (enter_score % 10) <= 6:
    print('A')
elif enter_score < 100 and 6 < (enter_score % 10) <= 9:
    print('A+')
elif enter_score == 100:
    print('A+')
