# entered decimal number, print out 2~32 number

def card_conv(x: int, r: int) -> str:
    """converse integer x to r number and return the array"""
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r
    
    return d[::-1]