# create 'n' random numbers between 10 and 99 (stop when 13)
import random
n = int(input('how many: '))

for _ in range(n):
    r = random.randint(10,99)
    print(r, end=' ')
    if r == 13:
        print('\n stop program')
        break

else:
    print('\n stop create random numbers')