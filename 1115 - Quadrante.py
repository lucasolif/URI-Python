y = 1
x = 1

while y != 0 and x != 0:

    y, x = input().split()
    y = int(y)
    x = int(x)

    if x == 0 or y == 0:
        break
    if x > 0:
        if y > 0:
            print("primeiro")
        if y < 0:
            print("segundo")
    if x < 0:
        if y < 0:
            print("terceiro")
        if y > 0:
            print("quarto")