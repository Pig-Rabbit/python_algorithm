# print the maximum of sequence elements (elements are entered)

import random
from max import max_of

print('calculate the maximum of array')
num = int(input('enter the number of random: '))
lo = int(input('enter the minimum of random: '))
hi = int(input('enter the maximum of random: '))
x = [None]*num

for i in range(num):
    x[i] = random.randint(lo, hi) # give random number between lo and hi

print(f'{(x)}')
print(f'the maximum is {max_of(x)}.')