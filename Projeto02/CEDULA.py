valor = float(input("ESCREVA O VALOR DA COMPRA"))
pago = float(input("ESCREV O VALOR DO PAGAMENTO"))

troco = pago - valor

valorTotal = 1280

res = valorTotal - troco

nota200 = 0  #2
nota100 = 0  #4
nota50 = 0   #6
nota10 =0   #10
nota5 = 0   #10
nota1 = 0   #20
nota0_5 = 0 #20




while troco > 0:
        
    
        if troco >= 200:
            
            if nota200 < 2:
                
                nota200 += 1 
                troco-=200
                
        elif troco <= 200:
            
            if troco > 100:
                
                if nota100 < 4:
                    
                    nota100 += 1 
                    troco-=100
            elif troco <100:
                
                if troco > 50:
                    
                    if nota50 < 6:
                        
                        nota50 += 1 
                        troco-=50
                elif troco < 50:
                
                    if troco > 10:
                        
                        if nota10 < 10:
                            
                            nota10 += 1 
                            troco-=10
                    elif troco < 10:
                
                        if troco > 5:
                            
                            if nota5 < 10:
                                
                                nota5 += 1 
                                troco-=5
                        elif troco < 5:
                
                            if troco > 1:
                                
                                if nota1 < 20:
                                    
                                    nota1 += 1 
                                    troco-=1
                            elif troco < 1:
                                
                                if troco > 0.5:
                                    
                                    if nota0_5 < 20:
                                        
                                        nota0_5 += 1 
                                        troco-=0.5
                                
        
        
print(f"NOTA 200: {nota200}\nNOTA 100: {nota100}\nNOTA 50: {nota50}\nNOTA 10: {nota10}\nNOTA 5: {nota5}\nNOTA 1: {nota1}\nNOTA 0.5: {nota0_5}\nQUANTIDADE QUE RESTA NO CAIXA: {res} ")
    
            

