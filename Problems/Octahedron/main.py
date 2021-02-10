from math import pow, sqrt
a = int(input())

area = 2 * sqrt(3) * pow(a, 2)
volume = (1/3) * sqrt(2) * pow(a, 3)
print(round(area, 2), round(volume, 2))
