import math
num = int(input())
x = 1

for i in range(1, num + 1):
    print(f"{x} {pow(x, 2)} {pow(x, 3)}")
    x += 1