cont = 0
media = 0
for x in range(1,7):
    num = float(input())
    if num > 0:
        cont = cont + 1
        media = media + num
media = media / cont
print(f"{cont} valores positivos")
print(f"{media:.1f}")