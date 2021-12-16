valor = int(input())
if valor % 2 != 0:
    for i in range(1, valor + 1):
        if i % 2 != 0:
            print(i)
else:
    for i in range(1, valor):
        if i % 2 != 0:
            print(i)