# implementation non-recur quick sort

from fixed_stack import FixedStack
from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    range = FixedStack(right-left+1)
    range.push((left, right))
    while not range.is_empty():
        pl, pr = left, right = range.pop()
        x = a[(left + right)//2]

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push((left, pr))
        if pl < right:range.push((pl, right))

def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a)-1)

if __name__ == '__main__':
    print('start quick sort')
    num = int(input('enter the number of elements: '))
    x = [None]* num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    quick_sort(x)

    print('sort in ascending')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')