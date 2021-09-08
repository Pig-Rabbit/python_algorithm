# print * with the shape of  isosceles triagle

print('print isosceles triagle with left down right angle')
n = int(input('enter the length of short: '))

for i in range(n):
    for j in range(i+1):
        print('*', end = '')
    print()