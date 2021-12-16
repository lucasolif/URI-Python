segundo= int(input())
horas= segundo//3600
minutos= (segundo%3600)//60
segundos= segundo-(horas*3600)-(minutos*60)
print(f"{horas}:{minutos}:{segundos}")

