# use linked list class "linked_list"

from enum import Enum
from linked_list import LinkedList

Menu = Enum('Menu', ['add_first','add_last','remove_first',
                     'remove_last','print_current_node','next',
                     'remove_current_node','remove','search','membership',
                     'print','scan','exit'])

def select_Menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = ' ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = LinkedList()

while True:
    menu = select_Menu()

    if menu == Menu.add_first:
        lst.add_first(int(input('enter the value: ')))
    
    elif menu == Menu.add_last:
        lst.add_last(int(input('enter the value: ')))
    
    elif menu == Menu.remove_first:
        lst.remove_first()

    elif menu == Menu.remove_last:
        lst.remove_last()

    elif menu == Menu.print_current_node:
        lst.print_current_node()
    
    elif menu == Menu.next:
        lst.next()
    
    elif menu == Menu.remove_current_node:
        lst.remove_current_node()
    
    elif menu == Menu.remove:
        lst.remove()

    elif menu == Menu.search:
        pos = lst.search(int(input('enter the value to search: ')))
        if pos >= 0:
            print(f'the value is located at {pos + 1}')
        else:
            print('the value doesn\'t exist')
        
    elif menu == Menu.membership:
        print('the value '
              +('is' if int(input('enter the value: ')) in lst else 'is not') + ' included')
    
    elif menu == Menu.print:
        lst.print()

    elif menu == Menu.scan:
        for e in lst:
            print(e)
    
    else:
        break