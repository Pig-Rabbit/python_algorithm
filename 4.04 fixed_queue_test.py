# Use fixed length queue class "FixedQueue"

from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['Enque', 'Deque', 'Peek', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = ' ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'the number of data: {len(q)} / {q.capacity}')
    menu = select_menu()
    
    if menu == Menu.Enque:
        x = int(input('the enque data: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('queue is full')
        
    elif menu == Menu.Deque:
        try:
            x = q.deque()
            print(f'the deque data is {x}.')
        except FixedQueue.Empty:
            print('queue is empty')
    
    elif menu == Menu.Peek:
        try:
            x = q.peek()
            print(f'the peek data is {x}.')
        except FixedQueue.Empty:
            print('queue is empty')

    elif menu == Menu.Search:
        x = int(input('Enter the value for searching: '))
        if x in q:
            print(f'include {q.count(x)} number, and located in {q.find(x)}.')
        else:
            print('cannot find the value')

    elif menu == Menu.Dump:
        q.dump()

    else:
        break