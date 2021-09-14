# Use fixed length stack class "FixedStack"

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['Push', 'Pop', 'Peek', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = ' ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)

while True:
    print(f'the number of data: {len(s)} / {s.capacity}')
    menu = select_menu()
    
    if menu == Menu.Push:
        x = int(input('Enter data: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('stack is full')
        
    elif menu == Menu.Pop:
        try:
            x = s.pop()
            print(f'the pop data is {x}.')
        except FixedStack.Empty:
            print('stack is empty')
    
    elif menu == Menu.Peek:
        try:
            x = s.peek()
            print(f'the peek data is {x}.')
        except FixedStack.Empty:
            print('stack is empty')

    elif menu == Menu.Search:
        x = int(input('Enter the value for searching: '))
        if x in s:
            print(f'include {s.count(x)} number, and located in {s.find(x)}.')
        else:
            print('cannot find the value')

    elif menu == Menu.Dump:
        s.dump()

    else:
        break