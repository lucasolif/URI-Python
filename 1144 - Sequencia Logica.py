import math
num = int(input())
x = 1

while x <= num:
    print(f"{x} {pow(x, 2)} {pow(x, 3)}")
    print(f"{x} {pow(x, 2)+1} {pow(x, 3) + 1}")
    x += 1