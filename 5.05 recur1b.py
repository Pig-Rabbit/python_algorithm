# implementation recursive function with stack (remove recursive)

from fixed_stack import FixedStack

def recur(n: int) -> int:
    s = FixedStack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n-1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break

x = int(input('enter integer: '))

recur(x)