luku = 0
pienin = -1
while luku >= 0:
    print("Anna positiivinen numero (lopetus negatiivisella luvulla)")
    luku = int( input() )
    if pienin == -1:
        pienin = luku
    if luku <= pienin and luku >= 0:
        pienin = luku

if pienin != -1:
    print("Pienin antamasi luku oli ")
    print(pienin)
else:
    print("Et antanut lukuja.")