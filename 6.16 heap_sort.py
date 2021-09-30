# implementation heap sort algorithm

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        '''heap sort from a[left] ~ a[right]'''
        temp = a[left]

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n-1) // 2, -1, -1):
        down_heap(a, i, n-1)

    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)

if __name__ == '__main__':
    print('start heap sort')
    num = int(input('enter the number of elements: '))
    x = [None]*num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    heap_sort(x)

    print('sort in ascending')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

