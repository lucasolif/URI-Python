n= 1
soma= 0
i= 0
while True:
    n = int(input())
    if n >= 0:
        soma += n
        i += 1
        media= soma/i
    else:
        break
print("{:.2f}".format(media))