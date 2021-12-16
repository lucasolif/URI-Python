num = int(input())
contIn = 0
contOut= 0

for i in range(1, num + 1):
    x = int(input())
    if x >= 10 and x <= 20:
        contIn += 1
    else:
        contOut += 1

print(f"{contIn} in")
print(f"{contOut} out")