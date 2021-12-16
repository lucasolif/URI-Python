dia1,Ndia1= input().split()
h1,m1,s1= map(int,input().split(' : '))

dia2,Ndia2= input().split()
h2,m2,s2= map(int,input().split(' : '))

Ndia1= int(Ndia1)
Ndia2= int(Ndia2)

total_segundos =((Ndia2*86400)+(h2*3600)+(m2*60)+(s2)) - ((Ndia1*86400)+(h1*3600)+(m1*60)+(s1))
dias= total_segundos//86400
horas= (total_segundos%86400)//3600
minutos= ((total_segundos%86400)%3600)//60
segundos= total_segundos-(dias*86400)-(horas*3600)-(minutos*60)

print(dias,"dia (s)")
print(horas,"hora (s)")
print(minutos,"minuto (s)")
print(segundos,"segundo (s)")
