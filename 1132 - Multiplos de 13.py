num1 = int(input())
num2 = int(input())
soma = 0

if num1 < num2:
    for x in range(num1, num2+1):
        if x % 13 != 0:
            soma += x
    print(f"{soma}")

if num1 > num2:
    for x in range(num2, num1+1):
        if x % 13 != 0:
            soma += x
    print(f"{soma}")