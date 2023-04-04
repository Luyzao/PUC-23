#Primeiro Passo - Abrir o caixa

print(f"\tBem-Vindo!!!")

password_correta = int(input("DEFINA SUA SENHA: "))
ten = 3

while ten > 0:

        password = int(input("Dígite sua senha para abrir o caixa: "))
        
        if password != password_correta:
        
            if ten == 1:
                break
            else:
                ten -= 1
            print(f"VC TEM DIREITO A MAIS {ten} TENTATIVAS")
             
        else:
            ten = 0
            print(f"Senha Correta \n Caixa Aberto!")
            print(f"Dinheiro para troco: R$1280,00")

            print("INSERÇÃO DOS ITENS VENDIDOS")

            val = 0
            itn = 0
            val_itn = 0
            total = 0
            tudo = 0

            while val == 0:
                itn += 1
                val_itn = float(input(f"Digite o valor do item {itn}: R$"))
                
                if val_itn > 0:

                    total = tudo
                    tudo = tudo + val_itn


                elif val_itn == 0:

                    ten_opc = 3

                    while ten_opc > 0: 

                        
                    
                        opc = input(f"Deseja Realmente Finalizar?? (S= Sim e N= Não)\n")
                        
                        if opc == "S" or opc =="s":
                            itn -= 1
                            print(f"Venda Finalizada com {itn} itens")
                            print(f"Valor total da compra: R${tudo}")
                            val = 1
                            ten_opc = 0

                            pagar = float(input("Insira a quantia para fazer o pagaemnto: "))

                            troco = pagar - tudo
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
 


                            
                        elif opc == "N" or opc == "n":
                            itn -=1
                            val = 0
                            ten_opc = 0
                        else:

                            ten_opc -= 1

                            if ten_opc == 0:
                                 print("Tentativas demais, Ecerranto programa... ")
                                 exit() 

                            else:
                                print("Opção não existe, tente novamente")
                                print(f"Tentativas restantes {ten_opc}")


                elif val_itn == -1:
                         
                    itn -= 1
                
                    print(f"Escreva o valor correto do iten {itn}: R$")

                    tudo = total
                    

                         
                         
