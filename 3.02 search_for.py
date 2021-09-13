# linear algorithm with 'for'

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
        return -1

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