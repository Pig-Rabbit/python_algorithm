# implementation pure recursive function

def recur(n: int) -> int:
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)
    
x = int(input('enter integer: '))

recur(x)