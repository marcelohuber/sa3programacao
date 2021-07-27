print("=" *30); print("{:^30}".format("Calculadora")); print("=" *30)
total = input("Valor Total das compras R$ "); total = float(total)
receb = input("Valor Recebido R$ "); troco = float(receb) - total
vTro = round(float(troco),2); print(" O Valor do Troco é ",vTro)
vCed = 50; qCed=0; vlrC=0; qtdC=0
while True:
    if vTro >= vCed: vTro -= vCed; qCed += 1; vlrC += vCed; qtdC += 1
    else:
        if qCed > 0: print (qCed, "Cedulas de R$" ,vCed); qCed = 0
        elif vCed == 50: vCed = 20
        elif vCed == 20: vCed = 10
        elif vCed == 10: vCed = 5
        elif vCed == 5: vCed = 2
        elif vCed == 2: break
vMoe = 1.00; qMoe=0; vlrM=0.0; qtdM=0
while True:
    v1 = int(round(vTro*100,0)) - int(round(vMoe*100,0))
    if v1 >= 0 : vTro -= vMoe; qMoe += 1; vlrM += vMoe; qtdM += 1
    else:
        if qMoe > 0: print (qMoe,"Moedas R$",vMoe); qMoe = 0
        elif vMoe == 1.00: vMoe = 0.50
        elif vMoe == 0.50: vMoe = 0.25
        elif vMoe == 0.25: vMoe = 0.10
        elif vMoe == 0.10: vMoe = 0.05
        else: break
vlrC = round(float(vlrC),2); vlrM = round(float(vlrM),2)
if vlrC >0: print (" R$ ",vlrC,"em",qtdC,"Cedulas")
if vlrM >0: print (" R$  ",vlrM,"em",qtdM,"Moedas")
tCM = vlrC+vlrM; print (" R$",tCM,"= TOTAL")
