valor = int(input())

nota100 = valor//100
nota50 = valor%100//50
nota20 = valor%100%50//20
nota10 = valor%100%50%20//10
nota05 = valor%100%50%20%10//5
nota02 = valor%100%50%20%10%5//2
nota01 = valor%100%50%20%10%5%2//1

print(valor)
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota05} nota(s) de R$ 5,00")
print(f"{nota02} nota(s) de R$ 2,00")
print(f"{nota01} nota(s) de R$ 1,00")