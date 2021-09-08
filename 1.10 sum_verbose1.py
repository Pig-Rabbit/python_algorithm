# the sum of integer from a to b (1)
print('solve the sum of integer from a to b')
a = int(input('enter integer a:'))
b = int(input('enter integer b:'))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    if i < b:
        print(f'{i} + ', end = '')
    else:
        print(f'{i} = ', end = '')
    sum += i

print(sum)