# implementation recursive function with non-recursive method (remove tail recursive)

def recur(n: int) -> int:
    while n > 0:
        recur(n-1)
        print(n)
        n = n - 2
        
x = int(input('enter integer: '))

recur(x)