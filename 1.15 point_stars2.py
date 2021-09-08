# print * n times with changing row for w times *

print('print * out')
n = int(input('how many: '))
w = int(input('change row for: '))

for _ in range(n//w):
    print('*'*w)
    
rest = n%w
if rest:
    print('*'*rest)