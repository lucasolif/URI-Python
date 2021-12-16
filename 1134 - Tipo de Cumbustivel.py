qtdAlcool = 0
qtdGasolina = 0
qtdDiesel = 0
stop = True


while stop == True:
    cod = int(input())
    if cod == 1:
        qtdAlcool += 1
    elif cod == 2:
        qtdGasolina += 1
    elif cod == 3:
        qtdDiesel += 1
    elif cod == 4:
        stop = False

print("MUITO OBRIGADO")
print(f"Alcool: {qtdAlcool}")
print(f"Gasolina: {qtdGasolina}")
print(f"Diesel: {qtdDiesel}")