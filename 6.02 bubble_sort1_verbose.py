# implementation bubble sorting algorithm (print out the sorting process)

from typing import MutableSequence

def bubble_sort_verbose(a: MutableSequence) -> None:
    ccnt = 0 # compare sequence
    scnt = 0 # change sequence
    n = len(a)
    for i in range(n-1):
        print(f'pass {i+1}')
        for j in range(n-1, i, -1):
            for m in range(0, n-1):
                print(f'{a[m]:2}' + ('  ' if m != j-1 else
                                     ' +' if a[j-1] > a[j] else
                                     ' -'), end = '')
            print(f'{a[n-1]:2}')
            ccnt += 1
            if a[j-1] > a[j]:
                scnt += 1
                a[j-1], a[j] = a[j], a[j-1]
        for m in range(0, n-1):
            print(f'{a[m]:2}', end = '  ')
        print(f'{a[n-1]:2}')
    print(f'compare {ccnt} times')
    print(f'change {scnt} times')
    
if __name__ == '__main__':
    print('bubble sorting start')
    num = int(input('enter the number of element: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort_verbose(x)

    print('enumerate the elements in ascending')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')