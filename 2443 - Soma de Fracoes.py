a,b,c,d = map(int,input().split())
resultadoa = 0
resultadob = 0
teste = 0
if((a >= 1) and (a <= 100) and (b >= 1) and (b <= 100) and (c >= 1) and (c <= 100) and (d >= 1) and (d <= 100)):
    resulta = (a * d) + (c * b)
    resultb = b * d
    A = resulta
    B = resultb
    while B != 0:
        teste = A % B
        A = B
        B = teste
        result1 = int(resulta / A)
        result2 = int(resultb / A)
print(result1, result2)