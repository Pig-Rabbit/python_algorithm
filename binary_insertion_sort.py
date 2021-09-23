# implementation binary insertion sort algorithm

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        
        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j-1]
        a[pd] = key
    
if __name__ == '__main__':
    print('binary insertion sort start')
    num = int(input('enter the number of element: '))
    x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

binary_insertion_sort(x)

print('enumerate the elements in ascending')
for i in range(num):
    print(f'x[{i}] = {x[i]}')
