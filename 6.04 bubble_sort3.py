# implementation bubble sorting algorithm (update algorithm 2)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    '''reduce the scan extent'''
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last
    
if __name__ == '__main__':
    print('bubble sorting start')
    num = int(input('enter the number of element: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)

    print('enumerate the elements in ascending')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')