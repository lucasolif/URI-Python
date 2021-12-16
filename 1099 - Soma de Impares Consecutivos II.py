n = int(input())



for i in range(1, n+1):
    num = input().split()
    num1, num2 = num
    num1 = int(num1)
    num2 = int(num2)
    soma = 0
    if num1 < num2:
        for j in range(num1+1, num2):
            if j % 2 == 1:
                soma += j
    if num1 > num2:
        for j in range(num2+1, num1):
            if j % 2 == 1:
                soma += j
    if num1 == num2:
        soma = 0
    print(f"{soma}")










