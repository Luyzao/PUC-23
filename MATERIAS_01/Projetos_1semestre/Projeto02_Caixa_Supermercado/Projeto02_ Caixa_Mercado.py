#Projeto elaborado na disciplina de algoritmos de programacao. 
#Programa para caixa de supermercado

# ------------------------------------------------------------------------------------------------------------
#ANA CAROLINA MORELLI CHAVES 23017617
#CICERA EDUARDA DA COSTA 23016727
#LUIZ GUSTAVO PINTO DA SILVA 23013028
# ------------------------------------------------------------------------------------------------------------

# ABRINDO CAIXA(PEDINDO NOVA SENHA PARA USUARIO E DEPOIS VERIFICANDO A SENHA DEFINIDA)

print(f"\n\t||||||||||||||||||||||||||\n\t|| B e m - V i n d o!!! ||\n\t||||||||||||||||||||||||||\n")

# Variavel para deifinir a senha do caixa
senha = '1234'

# Variavel para quantidade de tentativas
ten =3 

# Sistema para verificar a senha com limite de tentativas
while ten > 0:


    verificar_senha = input(f"\n\t Dígite a senha do caixa: ")

    
    verificar_senha = int(input(f"\t Dígite a senha do caixa: "))


    if type(verificar_senha) == int:

        if senha != verificar_senha:
            
            if ten == 1:
                print("\t--REINICIE O PROGRAMA E TENTE NOVAMENTE--")
                break

            else:
                ten -= 1
                print(f"\n\t VC TEM DIREITO A MAIS {ten} TENTATIVAS")
        else:
    
    
        

# SISTEMA DO CAIXA

            ten=0

        print(f"\n\t||||||||||||||||||||||||||||||||\n\t|| C a i x a - A b e r t o!!! ||\n\t||||||||||||||||||||||||||||||||\n")
        print(f' \tTroco disponivel no caixa: 1280,00')

        trocoTotal = 1280
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
                val_itn = float(input(f"\n\tDigite o valor do item{itn}: R$"))

                if val_itn > 0:

                    total = tudo
                    tudo = tudo + val_itn


                elif val_itn == 0:
                    
                    controle = 0
                    
                    while controle == 0:

                        opc = input(f"\n\n\tDeseja Realmente Finalizar?? (S= Sim e N= Não): ")
                                    
                        if opc == "S" or opc =="s":
                                        
                            itn -= 1
                            controle = 1

                            
                            print(f"\n\t||||||||||||||||||||||||||||||||||||\n\t|| Venda Finalizada com {itn} itens   ||")
                            print(f"\t|| Valor total da compra: R${tudo} ||\n\t||||||||||||||||||||||||||||||||||||\n")


                            pessoa += 1
                            somaTotal += tudo
                            itn = 0
                            ten_opc = 0
                            
                            controle1 = 0

                            while controle1 == 0:

                                    pagar = float(input(f"\tInsira a quantia para fazer o pagamento: R$"))

                                    if pagar > 0:

                                        troco = pagar - tudo
                                        
                                        if pagar >= tudo:
                                        
                                            if troco <= 300:

                                                valorTotal = 1280
                                                tudo = 0

                                                if trocoTotal > troco:
                                                    
                                                   
                                                    trocoTotal -= troco
                                                    controle1 = 1
                                                    print(f"\n\tValor do troco: R${troco}\n")
                                                    controle2 = 0
                                                
                                                else:
                                                    print("\n\n\n\t-- O TROCO DO CAIXA ACABOU CHAME O GERENTE --\n\n\tEncerrando sistema.....\n\n")
                                                    controle1 = 1
                                                    controle = 1
                                                    controle2 = 1
                                                    val = 1
                                                    
                                            
                                                
                                            
                                            else:
                                                print (f"\n\t --VALOR DO TROCO ACIMA DO PERMITIDO-- \n")
                                            
                                        else:
                                            print (f"\n\t --VALOR DIGITADO INSUFICIENTE PARA PAGAMENTO-- \n")
                                            
                                    else:
                                        print (f"\n\t --VALOR DIGITADO INSUFICIENTE PARA PAGAMENTO-- \n")
                                            


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

                                
                            if controle2 == 0:

                                print('\t||||||||||||||||||||||\n\t||       TROCO      ||\n\t||||||||||||||||||||||')                   

                                if nota200 != 0:
                                        
                                    print(f"\t|| Notas de 200: {nota200}  ||")
                                        
                                if nota100 != 0:
                                        
                                    print(f"\t|| Notas de 100: {nota100}  ||")
                                    
                                if nota50 != 0:
                                        
                                    print(f"\t|| Notas de 50: {nota50}   ||")

                                if nota10 != 0:
                                        
                                    print(f"\t|| Notas de 10: {nota10}   ||")
                                    
                                if nota5 != 0:
                                        
                                    print(f"\t|| Notas de 5: {nota5}    ||")

                                if nota1 != 0:
                                        
                                    print(f"\t|| Moedas de 1: {nota1}   ||")

                                if nota0_5 != 0:
                                        
                                    print(f"\t|| Moedas de 0.5: {nota0_5}  ||")
                                        
                                if troco == pagar:
                                    print(f"\t||     SEM TROCO    ||")

                                print('\t||||||||||||||||||||||')    
                            
                            

    # FECHAMENTO DO CAIXA 
                            
                            while controle2 == 0:
                            
                                opc = input(f"\n\tDESEJA FECHAR O CAIXA? (S= Sim e N= Não)")

                                if opc == "S" or opc =="s":

                                    controle2 = 1
                                                
                                    print(f"\n\t||||||||||||||||||||||||||||\n\t|| FECHAMENTO DO CAIXA!!! ||\n\t||||||||||||||||||||||||||||\n\n")
                                    print("\tInformações: ")
                                    print(f"\n\t|||||||||||||||||||||||||||||||||||||\n\t|| Número de cliente: {venda}            ||")
                                    print(f"\t|| Valor total das Vendas: R${somaTotal} ||\n\t|||||||||||||||||||||||||||||||||||||")
                                    print(f"\t|| Valor existente no caixa: {trocoTotal}||")

                                    nota200 = 0
                                    res200 = 2

                                    nota100 = 0
                                    res100 = 4

                                    nota50 = 0
                                    res50 = 6

                                    nota10 = 0
                                    res10 = 10

                                    nota5 = 0
                                    res5 = 10

                                    nota1 = 0
                                    res1 = 20

                                    nota0_5 = 0
                                    res0_5 = 20

                                    trocoTotal = valorTotal - trocoTotal


                                    while trocoTotal > 0:
                    
                                        if trocoTotal >=200 and nota200 < 2:

                                            trocoTotal -= 200
                                            nota200+=1
                                            
                                        
                                                        
                                        elif trocoTotal >= 100 and nota100 < 4:

                                            trocoTotal -= 100
                                            nota100+=1
                                        

                                        elif trocoTotal >= 50 and nota50 < 6:

                                            trocoTotal -= 50
                                            nota50+=1
                                        

                                        elif trocoTotal >= 10 and nota10 < 10:

                                            trocoTotal -= 10
                                            nota10+=1
                                            

                                        elif trocoTotal >= 5 and nota5 < 10:

                                            trocoTotal -= 5
                                            nota5+=1
                                            
                                                    

                                        elif trocoTotal >= 1 and nota1 < 20:

                                            trocoTotal -= 1
                                            nota1+=1
                                            

                                        elif trocoTotal >= 0.5 and nota0_5 < 20:

                                            trocoTotal -= 0.5
                                            nota0_5+=1

                                    res200 -= nota200
                                    res100 -= nota100
                                    res50 -= nota50
                                    res10 -= nota10
                                    res5 -= nota5
                                    res1 -= nota1
                                    res0_5 -= nota0_5
                                    

                                    if res200 != 0:
                                        
                                        print(f"\t|| Notas de 200: {res200}                 ||")
                                        
                                    if res100 != 0:
                                        
                                        print(f"\t|| Notas de 100: {res100}                 ||")
                                    
                                    if res50 != 0:
                                        
                                        print(f"\t|| Notas de 50: {res50}                  ||")

                                    if res10 != 0:
                                        
                                        print(f"\t|| Notas de 10: {res10}                 ||")
                                    
                                    if res5 !=0:
                                        
                                        print(f"\t|| Notas de 5: {res5}                  ||")

                                    if res1 != 0:
                                        
                                        print(f"\t|| Moedas de 1: {res1}                 ||")

                                    if res0_5 != 0:
                                        
                                        print(f"\t|| Moedas de 0.5: {res0_5}               ||")

                                    print('\t|||||||||||||||||||||||||||||||||||||')    

                                    print("\n\tAté breve........\n\n")

                                    val = 1

                                elif opc == "N" or opc == "n":
                                                
                                    print(f'\n\tCONTINUANDO VENDAS...\n')

                                    venda += 1

                                    print(f"\n\t||||||||||||||||||||||||||||||||||||\n\t|| INSIRA OS VALORES DA {venda}° COMPRA ||\n\t||||||||||||||||||||||||||||||||||||")

                                    controle2 = 1
                                    
                                else :
                                    print("\n\t-- VALOR INVALIDO --\n")
                                                

                                            
                        elif opc == "N" or opc == "n":
                        
                            itn -=1
                            val = 0
                            ten_opc = 0
                            controle = 1
                            
                            
                        else :
                            print("\n\t-- VALOR INVALIDO --\n")
                            

                elif val_itn == -1:
                                
                    itn -= 2

                    tudo = total
                    
                elif val_itn < -1:
                    
                    print("\n\t-- VALOR INVALIDO --\n")
                    
                    itn -= 1

    else:
        print("\n\t-- VALOR INVALIDO --\n")

                

                    
                   






