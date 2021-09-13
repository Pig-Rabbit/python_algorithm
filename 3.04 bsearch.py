# binary search algorithm

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr)//2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input('enter the number of element: '))
    x = [None]*num
    
    print('enter array data in ascending')
    
    x[0] = int(input('x[0]: '))
    for i in range(1,num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break
    
    ky = int(input('enter the objective value: '))

    idx = bin_search(x,ky)

    if idx == -1:
        print("the objective doesn't exist")
    else:
        print(f"the objective is in x[{idx}]")