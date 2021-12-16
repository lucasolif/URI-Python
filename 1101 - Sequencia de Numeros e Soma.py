num1 = 1
num2 = 1

while num2 > 0 or num1 > 0:
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    soma = 0
    if num1 < num2:
        if num2 <= 0 or num1 <= 0:
            break
        for x in range(num1, num2+1):
            soma += x
            print(f"{x}", end=" ")
        print(f"Sum={soma}")
    if num1 > num2:
        if num2 <= 0 or num1 <= 0:
            break
        for x in range(num2, num1+1):
            soma += x
            print(f"{x}", end=" ")
        print(f"Sum={soma}")
