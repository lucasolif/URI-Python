quantTeste = int(input())
contCoelho = 0
contRato = 0
contSapo = 0


for i in range(1, quantTeste + 1):
    x = input().upper().split()
    a, b = x

    if b == 'C':
        contCoelho += int(a)
    elif b == 'R':
        contRato += int(a)
    elif b == 'S':
        contSapo += int(a)
totalCobaia = contSapo + contRato + contCoelho

porcCoelho = (contCoelho/totalCobaia) * 100
porcRato = (contRato/totalCobaia) * 100
porcSapo = (contSapo/totalCobaia) * 100

print(f"Total: {totalCobaia} cobaias")
print(f"Total de coelhos: {contCoelho}")
print(f"Total de ratos: {contRato}")
print(f"Total de sapos: {contSapo}")
print(f"Percentual de coelhos: {porcCoelho :.2f} %")
print(f"Percentual de ratos: {porcRato :.2f} %")
print(f"Percentual de sapos: {porcSapo :.2f} %")