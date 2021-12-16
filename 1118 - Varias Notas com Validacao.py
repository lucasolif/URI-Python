cont = 0
media = 0
op = 1
continuar = True


while continuar == True:
    nota = float(input())
    if (nota >= 0) and (nota <= 10):
        media += nota
        cont += 1
        if cont == 2:
            media /= 2
            print(f"media = {media:.2f}")

            media = 0
            cont = 0
            while True:
                print("novo calculo (1-sim 2-nao)")
                novo = int(input())

                if novo == 2:
                    continuar = False
                    break
                elif novo == 1:
                    continuar == True
                    break
    else:
        print("nota invalida")
