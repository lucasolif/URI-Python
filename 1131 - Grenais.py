qtdVitoInter = 0
qtdVitoGremio = 0
empate = 0


while True:
    golInter, golGremio = list(map(int,input().split()))
    if golGremio == golInter:
        empate += 1
    else:
        if golInter > golGremio:
            qtdVitoInter += 1
        else:
            qtdVitoGremio += 1

    print("Novo grenal (1-sim 2-nao)")
    novo = int(input())
    if novo == 2:
        break

print(f"{qtdVitoInter + qtdVitoGremio + empate} grenais")
print(f"Inter:{qtdVitoInter}")
print(f"Gremio:{qtdVitoGremio}")
print(f"Empates:{empate}")
if qtdVitoGremio == qtdVitoInter:
    print("Nao houve vencedor")
else:
    if qtdVitoInter > qtdVitoGremio:
        print("Inter venceu mais")
    else:
        print("Gremio venceu mais")


