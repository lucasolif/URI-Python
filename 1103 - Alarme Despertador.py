while True:
    n= list(map(int,input().split()))
    h1 = n[0]
    m1 = n[1]
    h2 = n[2]
    m2 = n[3]
    hora_inicial = 0
    hora_final = 0
    if (h1 + m1 + h2 + m2) == 0:
        break
    if h1 == 0:
        hora_inicial = 24
    else:
        hora_inicial = h1
    if h2 == 0:
        hora_final = 24
    else:
        hora_final = h2
    hora_inicial= (hora_inicial*60) + m1
    hora_final= (hora_final*60) + m2

    if hora_final > hora_inicial:
        print(hora_final-hora_inicial)
    else:
        print((24*60)-(hora_inicial-hora_final))