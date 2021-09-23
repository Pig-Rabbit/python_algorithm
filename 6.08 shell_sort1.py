# implementation shell sort algorithm

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = n//2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2

if __name__ == '__main__':
    print('shell sort start')
    num = int(input('enter the number of element: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)

    print('enumerate the elements in ascending')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')