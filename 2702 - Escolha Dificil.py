frango, bife, massa=map(int,input().split())
pedi_frango, pedi_bife, pedi_massa=map(int,input().split())

if pedi_frango > frango and pedi_bife > bife and pedi_massa > massa:
    sem_refeicao= (pedi_frango-frango)+(pedi_bife-bife)+(pedi_massa-massa)
    print(sem_refeicao)
elif pedi_frango < frango and pedi_bife > bife and pedi_massa > massa:
    sem_refeicao= (pedi_bife-bife)+(pedi_massa-massa)
    print(sem_refeicao)
elif pedi_frango < frango  and pedi_bife < bife and pedi_massa > massa:
    sem_refeicao= pedi_massa-massa
    print(sem_refeicao)
elif pedi_frango < frango and pedi_bife > bife and pedi_massa < massa:
    sem_refeicao= pedi_bife-bife
    print(sem_refeicao)
elif pedi_frango > frango and pedi_bife < bife and pedi_massa < massa:
    sem_refeicao= pedi_frango-frango
    print(sem_refeicao)
elif pedi_frango > frango and pedi_bife < bife and pedi_massa > massa:
    sem_refeicao=(pedi_frango-frango) + (pedi_massa-massa)
    print(sem_refeicao)
elif pedi_frango > frango and pedi_bife > bife and pedi_massa < massa:
    sem_refeicao=(pedi_frango-frango)+(pedi_bife-bife)
    print(sem_refeicao)
else:
    pedi_frango == frango and pedi_bife == bife and pedi_massa == massa
    print(0)