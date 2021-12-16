x= int(input())
for c in range(0, x):
    num= int(input())
    for i in range(2,num):
        if (num % i == 0):
            print("{} nao eh primo".format(num))
            break
        else:
            print("{} eh primo".format(num))
            break




