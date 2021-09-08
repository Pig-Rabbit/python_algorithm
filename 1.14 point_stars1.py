# print * n times with changing row for w times *

print('print * out')
n = int(input('how many: '))
w = int(input('change row for: '))

for i in range(n):
    print('*', end = '')
    if i % w == w-1:
        print()

if n % w:
    print()