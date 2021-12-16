salario= float(input())

if 0 < salario <= 400:
    reajuste = (salario * 15)/100
    print("Novo salario:","{:.2f}".format(salario + reajuste))
    print("Reajuste ganho:","{:.2f}".format(reajuste))
    print("Em percentual: 15 %")
elif 400 < salario <= 800:
    reajuste = (salario * 12)/100
    print("Novo salario:","{:.2f}".format(salario + reajuste))
    print(("Reajuste ganho:","{:.2f}".format(reajuste))
    print("Em percentual: 12 %")
elif 800 < salario <= 1200:
    reajuste = 