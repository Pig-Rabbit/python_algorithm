# entered decimal number, print out 2~32 number

def card_conv(x: int, r: int) -> str:
    """converse integer x to r number and return the array"""
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r
    
    return d[::-1]

if __name__ == '__main__':
    print('converse the number 10 to n')

    while True:
        while True:
            no = int(input("enter not negative value for conversion: "))
            if no > 0:
                break
        
        while True:
            cd = int(input("enter the number to converse: "))
            if 2 <= cd <= 36:
                break
        
        print(f'the number of {cd} is {card_conv(no, cd)}')

        retry = input ("one more time? (Y/N)")
        if retry in {'N', 'n'}:
            break