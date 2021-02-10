from math import exp

x = int(input())
print(round((1 / (1 + exp(-x))), 2))
