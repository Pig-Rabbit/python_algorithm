# divide the array into two groups

from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n - 1
    x = a[n//2] # pivot(center element)

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'pivot is {x}')
    print('the group below pivot')
    print(*a[0 : pl])
    if pl > pr + 1:
        print('the group is same with pivot')
        print(*a[pr + 1: pl])

    print('the group over pivot')
    print(*a[pr + 1: n])

if __name__ == '__main__':
    print('divide the array')
    num = int(input('enter the number of elements: '))
    x = [None]* num
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)