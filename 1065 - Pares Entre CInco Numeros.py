contPar = 0
contImpar = 0
contNegat = 0
contPositi = 0
for i in range(1,6):
    valor = float(input())
    if valor % 2 == 0:
        contPar += 1
        if valor > 0:
            contPositi += 1
        elif valor < 0:
            contNegat += 1
    else:
        contImpar += 1
        if valor > 0:
            contPositi += 1
        elif valor < 0:
            contNegat += 1

print(f"{contPar} valor(es) par(es)")
print(f"{contImpar} valor(es) impar(es)")
print(f"{contPositi} valor(es) positivo(s)")
print(f"{contNegat} valor(es) negativo(s)")