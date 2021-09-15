# implementation hanoi top

def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no - 1, x,  6 - x - y)
    print(f'move circle [{no}] from {x} to {y}.')

    if no > 1:
        move(no - 1, 6 - x - y, y)

print('implementation hanoi top')
n = int(input('enter the number of circle: '))
move(n, 1, 3)
    