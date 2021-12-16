import math
num = int(input())
poten = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        poten = pow(i,2)
        print(f"{i}^2 = {poten}")