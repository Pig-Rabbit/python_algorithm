# maximum value of 3 integers
print('find maximum with 3 integers')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'maximum value is {maximum}')