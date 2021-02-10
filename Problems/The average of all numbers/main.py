# put your python code here

n1 = int(input())
n2 = int(input())
counter = 0
sum_ = 0
for n in range(n1, n2 + 1):
    if abs(n % 3) == 0:
        sum_ += n
        counter += 1

print(sum_ / counter)
