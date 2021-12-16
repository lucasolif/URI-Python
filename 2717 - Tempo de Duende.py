min_falta= int(input())
p1,p2=map(int,input().split())

if (p1+p2) > min_falta:
    print("Deixa para amanha!")
else:
    print("Farei hoje!")