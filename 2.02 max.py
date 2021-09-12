# print maximum from sequence elements

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('calculate maximum of array')
    num = int(input('the number of element: '))
    x = [None]*num

    for i in range(num):
        x[i] = int(input(f'enter the value of x[{i}]: '))
    print(f'the maximum if {max_of(x)}')