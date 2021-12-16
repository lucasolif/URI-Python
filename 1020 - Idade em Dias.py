d= int(input())
anos= d//365
meses= (d%365)//30
dias= d-(anos*365)-(meses*30)
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")