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
nota1 = 0
nota0_5 = 0


while troco > 0:
        
    if troco >=200 and nota200 < 2:

        troco -= 200
        nota200 += 1
        

    elif troco >= 100 and nota100 < 4:

        troco -= 100
        nota100 += 1

    elif troco >= 50 and nota50 < 6:

        
        troco -= 50
        nota50 += 1

    elif troco >= 10 and nota10 < 10:

        troco -= 10
        nota10 += 1

    elif troco >= 5 and nota5 < 10:

        troco -= 5
        nota5 += 1
    

    elif troco >= 1 and nota1 < 20:

        troco -= 1
        nota1 += 1

    elif troco >= 0.5 and nota0_5 < 20:

        troco -= 0.5
        nota0_5 += 1
        
                
print(f"NOTA 200: {nota200}\nNOTA 100: {nota100}\nNOTA 50: {nota50}\nNOTA 10: {nota10}\nNOTA 5: {nota5}\nNOTA 1: {nota1}\nNOTA 0.5: {nota0_5}\nQUANTIDADE QUE RESTA NO CAIXA: {res} ")
 
            

