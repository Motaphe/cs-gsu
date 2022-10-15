''' First equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

for x in range(-10, 11):
    for y in range(-10, 11):
        if c == a*x + b*y and f == d*x + e*y:
            print (f"\nx={x}, y={y}")



