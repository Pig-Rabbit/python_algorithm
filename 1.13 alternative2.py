# alternative print + and -

print('print + and - alternatively')
n = int(input('how many: '))

for _ in range(n//2):
    print('+-', end = '')

if n % 2:
    print('+', end = '')

print()