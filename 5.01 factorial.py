# solve positive integer n factorial

def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('enter factorial to print out: '))
    print(f'the factorial of {n} is {factorial(n)}.')