# ABRINDO CAIXA(PEDINDO NOVA SENHA PARA USUARIO E DEPOIS VERIFICANDO A SENHA DEFINIDA)

print(f"\n\t||||||||||||||||||||||||||\n\t|| B e m - V i n d o!!! ||\n\t||||||||||||||||||||||||||\n")

# Variavel para deifinir a senha do caixa
senha = int(input(f"\n\t Defina uma nova senha de 4 digitos: "))

# Variavel para quantidade de tentativas
ten =3 

# Sistema para verificar a senha com limite de tentativas
while ten > 0:

    verificar_senha = int(input(f"\n\t Dígite a senha do caixa: "))

    if senha != verificar_senha:
        
        if ten == 1:
            break

        else:
            ten -= 1
            print(f"\n\t VC TEM DIREITO A MAIS {ten} TENTATIVAS")
    else:

# SISTEMA DO CAIXA

        ten=0

        print(f"\n\t||||||||||||||||||||||||||||||||\n\t|| C a i x a - A b e r t o!!! ||\n\t||||||||||||||||||||||||||||||||\n")
        print(f' \tTroco disponivel no caixa: 1280,00')


        venda =  1
        val = 0
        itn = 0
        val_itn = 0
        total = 0
        tudo = 0
        controle = 1
        pessoa = 0
        somaTotal = 0

       

# SISTEMA DA COMPRA DOS PRODUTOS


        print(f"\n\t||||||||||||||||||||||||||||||||||||\n\t|| INSIRA OS VALORES DA {venda}° COMPRA ||\n\t||||||||||||||||||||||||||||||||||||")
        while val == 0:

               
                

                itn += 1
                val_itn = float(input(f"\n\tDigite o valor do item {itn}: R$"))

                if val_itn > 0:

                    total = tudo
                    tudo = tudo + val_itn


                elif val_itn == 0:

                    ten_opc = 3

                    opc = input(f"\n\n\tDeseja Realmente Finalizar?? (S= Sim e N= Não): ")
                                
                    if opc == "S" or opc =="s":
                                    
                        itn -= 1

                        
                        print(f"\n\t||||||||||||||||||||||||||||||||||||\n\t|| Venda Finalizada com {itn} itens   ||")
                        print(f"\t|| Valor total da compra: R${tudo} ||\n\t||||||||||||||||||||||||||||||||||||\n")


                        pessoa += 1
                        somaTotal += tudo
                        itn = 0
                        ten_opc = 0

                        pagar = float(input(f"\tInsira a quantia para fazer o pagamento: "))

                        troco = pagar - tudo
                        valorTotal = 1280
                        res = valorTotal - troco
                        tudo = 0

# SISTEMA DE TROCO DO CAIXA

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


                        print('\t|||||||||||||||||||||||\n\t||       TROCO      ||\n\t|||||||||||||||||||||||')                   

                        if nota200 != 0:
                              
                              print(f"\t|| Notas de 200: {nota200}   ||")
                              
                        if nota100 != 0:
                              
                              print(f"\t|| Notas de 100: {nota100}   ||")
                        
                        if nota50 != 0:
                              
                              print(f"\t|| Notas de 50: {nota50}    ||")

                        if nota10 != 0:
                              
                              print(f"\t|| Notas de 10: {nota10}    ||")
                        
                        if nota5 != 0:
                              
                              print(f"\t|| Notas de 5: {nota5}     ||")

                        if nota1 != 0:
                              
                              print(f"\t|| Moedas de 1: {nota1}    ||")

                        if nota0_5 != 0:
                              
                              print(f"\t|| Moedas de 0.5: {nota0_5}  ||")

                        print('\t|||||||||||||||||||||||')    

        
                        opc = input(f"\n\tDESEJA FECHAR O CAIXA? (S= Sim e N= Não)")

                        if opc == "S" or opc =="s":
                                        print(f"\n\t||||||||||||||||||||||||||||\n\t|| FECHAMENTO DO CAIXA!!! ||\n\t||||||||||||||||||||||||||||\n\n")
                                        print("\tInformações: ")
                                        print(f"\n\t||||||||||||||||||||||||||||||||||\n\t|| Número de cliente: {venda}         ||")
                                        print(f"\t|| Valor total das Vendas: R${somaTotal} ||\n\t||||||||||||||||||||||||||||||||||")

                                        print("\n\tAté breve........\n\n")
                                        break

                        elif opc == "N" or opc == "n":
                                        print(f'\n\tCONTINUANDO VENDAS...\n')
                                        venda += 1
                                        print(f"\n\t||||||||||||||||||||||||||||||||||||\n\t|| INSIRA OS VALORES DA {venda}° COMPRA ||\n\t||||||||||||||||||||||||||||||||||||")

                                        controle += 1
                                        

                                    
                    elif opc == "N" or opc == "n":
                        itn -=1
                        val = 0
                        ten_opc = 0
         
                
                elif val_itn == -1:
                                
                    itn -= 1
                        
                    print(f"Escreva o valor correto do iten {itn}: R$")





