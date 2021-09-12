# print * with the shape of  isosceles triagle

print('print isosceles triagle with right down right angle')
n = int(input('enter the length of short: '))

for i in range(n):
    for _ in range(n-i-1):
        print(' ', end = '')
    for _ in range(i+1):
        print('*', end = '')
    print()