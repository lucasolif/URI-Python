x = 7
y = 4
z = -1
for i in range(1, 10, 2):
    for j in range(x, y, -1):
        print(f"I={i} J={j}")
    x += 2
    y += 2
