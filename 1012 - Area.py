import math
a, b, c = map(float, input().split())

areaTriangulo = (a * c)/2
areaCirculo = 3.14159 * pow(c, 2)
areaTrapezio = ((a + b) * c)/2
areaQuadrado = pow(b, 2)
areaRetangulo = a * b

print(f"TRIANGULO: {areaTriangulo:.3f}")
print(f"CIRCULO: {areaCirculo:.3f}")
print(f"TRAPEZIO: {areaTrapezio:.3f}")
print(f"QUADRADO: {areaQuadrado:.3f}")
print(f"RETANGULO: {areaRetangulo:.3f}")
