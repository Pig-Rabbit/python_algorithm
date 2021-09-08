# print multiplication table

print('-'*27)
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j}',end='')
    print()
print('-'*27)