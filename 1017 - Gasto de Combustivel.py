tempoViagem = int(input())
velocidadeMedia = int(input())

distancia = tempoViagem * velocidadeMedia
quantCombustivel = distancia/12
print(f"{quantCombustivel:.3f}")