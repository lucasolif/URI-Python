maior = 0
posi = 0
for i in range(1, 101):
    num = int(input())
    if num > maior:
        maior = num
        posi = i
print(maior)
print(posi)