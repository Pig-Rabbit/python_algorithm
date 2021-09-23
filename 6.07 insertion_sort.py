# implementation simple insert sort algorithm

from typing import MutableSequence

def insert_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':
    print('simple insert sorting start')
    num = int(input('enter the number of element: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insert_sort(x)

    print('enumerate the elements in ascending')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')