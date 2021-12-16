n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10

print("Media:","{:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif (media >= 5.0) and (media <= 6.9):
    print("Aluno em exame.")

    nota_exame = float(input())
    print("Nota do exame","{:.1f}".format(nota_exame))
    new_media = (nota_exame + media)/2
    if new_media >= 5.0:
        print("Aluno aprovado.")
    else:
        new_media <= 4.9
        print("Aluno reprovado.")
    print("Media final:","{:.1f}".format(new_media))


