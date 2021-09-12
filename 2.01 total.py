# print the sum and the average with 5 students score

print('calculate the sum and the average of student group')

score1 = int(input('the score of student 1: '))
score2 = int(input('the score of student 2: '))
score3 = int(input('the score of student 3: '))
score4 = int(input('the score of student 4: '))
score5 = int(input('the score of student 5: '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'the sum is {total}')
print(f'the average is {total/5}')