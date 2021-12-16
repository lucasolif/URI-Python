valor = float(input())

if 25 >= valor >= 0:
    print("Intervalo [0,25]")
elif 50 >= valor > 25:
    print("Intervalo (25,50]")
elif 75 >= valor > 50:
    print("Intervalo (50,75]")
elif 100 >= valor > 50:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")