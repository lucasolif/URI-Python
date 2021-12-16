def triangulo(a, b, c):
    if (abs(b-c) < a < b+c) or (abs(a-c) < b < a+c) or (abs(a - b) < c < a+b):
        if a == b == c:
            return 1
        if (a==b) and a!= c or (a==c)and c!=b or (c==b)and b!=a:
            return 2
        if a != b != c:
            return 3
    else:
        return 0

print("Informe os lados")

lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

result = triangulo(lado1, lado2, lado3)

if result == 1:
    print("Os lados [{}, {}, {}] representam um triangulo equilatero".format(lado1,lado2,lado3))
elif result == 2:
    print("Os lados [{}, {}, {}] representam um triangulo isosceles".format(lado1,lado2,lado3))
elif result == 3:
    print("Os lados [{}, {}, {}] representam um triangulo escaleno".format(lado1,lado2,lado3))
elif result == 0:
    print("Os lados [{}, {}, {}] nao representam um triangulo".format(lado1,lado2,lado3))
