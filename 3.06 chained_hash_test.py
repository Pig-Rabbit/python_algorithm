# use ChainedHash

from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['ADD', 'REMOVE', 'SEARCH', 'DUMP', 'EXIT'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end = '')
        n = int(input(': '))
        if 1<=n<=len(Menu):
            return Menu(n)

hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.ADD:
        key = int(input('enter ADD key: '))
        val = input('enter ADD value: ')
        if not hash.add(key,val):
            print('ADD failed')
    
    elif menu == Menu.REMOVE:
        key = int(input('enter REMOVE key: '))
        val = input('enter REMOVE value: ')
        if not hash.remove(key):
            print('REMOVE failed')
    
    elif menu == Menu.SEARCH:
        key = int(input('enter SEARCH key: '))
        t = hash.search(key)
        if t is not None:
            print(f'the value of the key is {t}')
        else:
            print('there are no value for searching')
    
    elif menu == Menu.DUMP:
        hash.dump()
    
    else:
        break
