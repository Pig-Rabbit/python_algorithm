# alternative print + and -

print('print + and i alternatively')
n = int(input('how many: '))

for i in range(n):
    if i % 2:
        print('-', end = '')
    else:
        print('+', end = '')

print()
