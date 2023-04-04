valor = float(input("ESCREVA O VALOR DA COMPRA"))
pago = float(input("ESCREV O VALOR DO PAGAMENTO"))

troco = pago - valor

valorTotal = 1280

res = valorTotal - troco

nota200 = 0
nota100 = 0
nota50 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0
nota0_5 = 0

duz = 0 
cem = 0
cin = 0
dez = 0
cinco = 0
dois = 0
um = 0
um50 = 0

while troco > 0:
        
    if troco >=200 and nota200 < 2:

        duz = int(troco/200)
        troco = troco - (duz * 200)
        nota200 += 1

    elif troco >= 100 and nota100 < 4:

        cem = int(troco/100)
        troco = troco - (cem * 100)
        nota100 += 1

    elif troco >= 50 and nota50 < 6:

        cin = int(troco/50)
        troco = troco - (cin * 50)
        nota50 += 1

    elif troco >= 10 and nota10 < 10:

        dez = int(troco/10)
        troco = troco - (dez * 10)
        nota10 += 1

    elif troco >= 5 and nota5 < 10:

        cinco = int(troco/5)
        troco = troco - (cinco * 5)
        nota5 += 1
    
    elif troco >= 2 and nota2 < 20:

        dois = int(troco/2)
        troco = troco - (dois * 2)
        nota2 += 1

    elif troco >= 1 and nota1 < 20:

        um = int(troco/1)
        troco = troco - (um * 1)
        nota1 += 1

    elif troco >= 0.5 and nota0_5 < 20:

        um50 = int(troco/0.5)
        troco = troco - (um50 * 0.5)
        nota0_5 += 1
        
                
print(f"NOTA 200: {duz}\nNOTA 100: {cem}\nNOTA 50: {cin}\nNOTA 10: {dez}\nNOTA 5: {cinco}\nNOTA 1: {um}\nNOTA 0.5: {um50}\nQUANTIDADE QUE RESTA NO CAIXA: {res} ")
    
            

