# implementation bubble sorting algorithm (update algorithm 1)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    '''stop algorithm if exchange sequence doesn't exist'''
    n = len(a)
    for i in range(n-1):
        exch = 0
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exch += 1
        if exch == 0:
            break
    
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