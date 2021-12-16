import numpy
while True:
    n= int(input())
    l=[]
    for i in range(n, 0, -1):
        l.append(i)
        print(l, end="")
        l=[]
        fat= numpy.prod(l)
        print(fat)
