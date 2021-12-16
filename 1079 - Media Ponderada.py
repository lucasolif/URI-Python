num = int(input())
media = 0


for i in range (1, num+1):
    n1, n2, n3 = map(float, input().split())
    media = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
    print(f"{media :.1f}")
