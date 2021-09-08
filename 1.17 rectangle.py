# enumerate the length of side for the rectangle with integer width and height
area = int(input('enter the area of rectangle: '))
for i in range(1, area+1):
    if i*i > area: break
    if area % i: continue
    print(f'{i} x {area // i}')