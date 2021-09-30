# implementation heat sort algorithm (use heapq.push and headq.pop)

import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)

if __name__ == '__main__':
    print('start heap sort with heapq')
    num = int(input('enter the number of elements: '))
    x = [None]*num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    heap_sort(x)

    print('sort in ascending')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
