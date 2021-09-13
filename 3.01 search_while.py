# linear search algorithm with 'while'

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    i = 0
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1

if __name__ == '__main__':
    num = int(input("enter the number of element: "))
    x = [None]*num
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    ky = int(input("enter the objective value: "))

    idx = seq_search(x, ky)

    if idx == -1:
        print("No element exist")
    else:
        print(f'the objective is located at x[{idx}]')