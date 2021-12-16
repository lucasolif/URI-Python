n = int(input())


for x in range(1, n+1):
    n1, n2 = map(int, input().split())

    if n2 != 0:
        div = n1/n2
        print(f"{div:.1f}")
    if n2 == 0:
        print("divisao impossivel")