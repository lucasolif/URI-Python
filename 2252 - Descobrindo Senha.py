cont = 0
while True:
    try:
        cont=cont+1
        digitos =int(input())
        oleo=list(map(float,input().split()))
        senha=""
        for i in range(digitos):

            indice = oleo.index (max(oleo))
            senha = senha + str(indice)
            oleo [indice] = -1

        print("Caso {}: {}".format(cont,senha))
    except:
        break
