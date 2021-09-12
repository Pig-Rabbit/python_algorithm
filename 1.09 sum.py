# the sum of integer from a to b (for)
print('solve the sum of integer from a to b')
a = int(input('enter a: '))
b = int(input('enter b: '))

if a > b:
    a, b = b, a # ascending sort

sum = 0
for i in range(a, b+1):
    sum += i

print(f'the sum of integer from {a} to {b} is {sum}')