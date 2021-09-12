# reverse line up of mutable sequence elements

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
    
if __name__ == '__main__':
    print('reverse line up')
    nx = int(input('the number of element: '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'enter the value of x[{i}]'))

    reverse_array(x)

    print('finish line up the array')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')