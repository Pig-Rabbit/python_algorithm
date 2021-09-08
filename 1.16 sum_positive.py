# sum of integer from 1 to n (n is positive)
print('solve the sum of integer from 1 to n')

while True:
    n = int(input('enter the value of n: '))
    if n > 0:
        break

sum = 0
for i in range(1, n+1):
    sum += i # add i to sum

print(f'the sum of integer from 1 to {n} is {sum}')