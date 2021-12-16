contador = 1
n = int(input())
while (n!=0):
    xb,yb,ub,vb = -10000,10000,10000,-10000
    for i in range(n):
        x,y,u,v = map(int,input().split())
        xb,yb,ub,vb = max(x,xb),min(yb,y),min(u,ub),max(vb,v)
    print("Teste", contador)
    contador = contador + 1
    if (xb <=ub and yb >= vb):
        print (xb,yb,ub,vb)
    else:
        print("nenhum")
    print()
    n = int(input())