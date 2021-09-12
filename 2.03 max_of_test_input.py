# print the maximum of sequence elements (elements are entered)

from max import max_of

print('calculate the maximum of array')
print('warning: exit with "End"')

number = 0
x = []

while True:
    s = input(f'enter the value of x[{number}]')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'enter {number} elements')
print(f'the maximum is {max_of(x)}.')