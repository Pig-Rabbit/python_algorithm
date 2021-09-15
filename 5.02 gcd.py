# solve greatest common divisor using Euclidean algorithm

def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == '__main__':
    print('solve the greatest common divisor of two integer')
    x = int(input('enter 1st integer: '))
    y = int(input('enter 2nd integer: '))
    print(f'the greatest common divisor of two integer is {gcd(x,y)}.125')