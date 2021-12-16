hi,mi,hf,mf = map(int, input().split())

if (hi < hf) and (mi < mf):
    h= (hf - hi)
    m= (mf - mi)
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
elif (hi > hf) and (mi > mf):
    h= (24 - hi) + hf
    m = (60 - mi) + mf
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))
elif (hi == hf) and (mi == mf):
    h= 24
    m= 0
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))
elif (hi == hf) and (mi < mf):
    h= 0
    m= (mf - mi)
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))
elif (hi < hf) and (mi == mf):
    h= (hf - hi)
    m= 0
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))
elif (hi < hf) and (mi > mf):
    h= (hf - hi)-1
    m= (60 - mi) + mf
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))
elif (hi > hf) and (mi < mf):
    h= (24 - hi) + hf
    m= (mf - mi)
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))
elif (hi > hf) and (mi == mf):
    h= (24 - hi) + hf
    m= 0
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))
elif (hi == hf) and (mi > mf):
    h= (24 - 1)
    m= (60 - mi) + mf
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))