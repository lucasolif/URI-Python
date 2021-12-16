num = int(input())

if num % 2 == 0:
    for i in range(num, num+12):
        if i % 2 != 0:
            print(f"{i}")
else:
    for i in range(num, num + 11):
        if i % 2 != 0:
            print(f"{i}")