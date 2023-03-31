#Primeiro Passo - Abrir o caixa

print(f"\tBem-Vindo!!!")

password_correta = 1234
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
                            print(f"Venda Finalizada {itn} itens")
                            print(tudo)
                            val = 1
                            ten_opc = 0
                            
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
   #FINALIZAÇÃO  DA VENDA E CALCULO DO TROCO:

            print("VENDA FINALIZADA")
            print(f"O valor total é: R$ {tudo:.2f}")

            val_pago = float(input(f"Valor pago: R$ "))
            troco = val_pago - tudo
            if troco == 0.00:
                print(f"NÃO HÁ TROCO")
            elif troco == 200 or 100 or 50 or 5 or 2 or 1 or 0.5:
                print(f"O valor do troco: R$ {troco:.2f} ")
                #falta especificar as cédulas do troco

#FECHAR O CAIXA:
            total_clientes = 0
            valtotal_vendas = 0
            valor_caixa = 0 
            opc2 = input(f"Deseja fechar o caixa? (S= Sim e N= Não)\n")

        if opc2 == "N" or "n":
                    print(f"Caixa não fechado!")
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
                                    print(f"Venda Finalizada {itn} itens")
                                    print(tudo)
                                    val = 1
                                    ten_opc = 0
                            
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
   #FINALIZAÇÃO  DA VENDA E CALCULO DO TROCO:

                    print("VENDA FINALIZADA")
                    print(f"O valor total é: R$ {tudo:.2f}")

                    val_pago = float(input(f"Valor pago: R$ "))
                    troco = val_pago - tudo
                    if troco == 0.00:
                        print(f"NÃO HÁ TROCO")
                    elif troco == 200 or 100 or 50 or 5 or 2 or 1 or 0.5:
                        print(f"O valor do troco: R$ {troco:.2f} ")
                #falta especificar as cédulas do troco
                #Essa não é a maneira mais clean de fazer o código, ficou bem confuso!

        elif opc2 == "S" or "s":
            print(f"Fechamento do caixa!!!")
            total_clientes += 1



