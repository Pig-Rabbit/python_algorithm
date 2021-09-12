# sum of integer from 1 to n (while)
print('solve the sum of integer from 1 to n')
n = int(input('enter the value of n: '))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(f'the sum of value from 1 to {n} is {sum}')