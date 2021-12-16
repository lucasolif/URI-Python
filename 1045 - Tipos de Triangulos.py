valores = map(float, input().split())
valores = list(valores) # Criei uma lista com os valores

A, B, C= sorted(valores, reverse=True ) # As variaveis "a, b, c" rceberam a lista "valores", depois usei o sorted para organizar a lista, como eu queria a lista em ordem decrescente usei o "reverse= True"


continua = True

if(A >= B+C):
    print("NAO FORMA TRIANGULO")
    continua = False

if(A**2 == (B**2) + (C**2) and continua):
    print("TRIANGULO RETANGULO")

if(A**2 > (B**2) + (C**2) and continua):
    print("TRIANGULO OBTUSANGULO")

if(A**2 < (B**2) + (C**2) and continua):
    print("TRIANGULO ACUTANGULO")

if(A == B and B == C and continua):
    print("TRIANGULO EQUILATERO")

if((A == B or B == C) and not (A == B and B == C) and continua):
    print("TRIANGULO ISOSCELES")