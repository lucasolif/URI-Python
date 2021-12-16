n1,n2,n3= map(int, input().split())

if n1 > n2 and n1 > n3:
    print(n1,"eh o maior")
if n2 > n1 and n2 > n3:
    print(n2,"eh o maior")
if n3 > n2 and n3 > n1:
    print(n3,"eh o maior")