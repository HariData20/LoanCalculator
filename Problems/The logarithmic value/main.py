from math import log

x = int(input())
y = int(input())

if y > 1:
    print(round(log(x, y), 2))
else:
    print(round(log(x), 2))
