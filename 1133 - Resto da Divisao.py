n1= int(input())
n2= int(input())

if n1 > n2:
    x = n2
    y = n1
elif n1 <= n2:
    x = n1
    y = n2
x = x + 1
while x < y:
    if x % 5 == 2 or x % 5 == 3:
        print(x)
    x = x + 1
