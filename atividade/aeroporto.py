#LUIZ GUSTAVO PINTO DA SILVA RA:23013028 // Ana Carolina Morelli Chaves RA:23017617

voos = {}

print("\n\n|| BEM VINDO AO FLYSKAY ||")

while True:
        
        print("\n1.Cadastrar novo voo\n2.Alterar info do voo\n3.Excluir voo\n4.Buscar voo\n5.Sair\n")

        try:

            menu = int(input("Opção: "))

        except:
            print("Está opção não existe")

        if menu == 1:
            print("\n--CADASTRANDO VOO--\n")
            controle = 1
            while controle == 1:

                while True:
                    try: 
                        cod = int(input("Código do voo: "))
                        if cod in voos.keys():
                            print("Este codigo já exite!!")
                        else:
                            break
                    except:
                        print("\nApenas números!!!\n")
                
                cidadeO = input("Cidade de origem: ")
                cidadeD = input("Cidade de destino: ")
                while True:
                    try:
                        NumE = int(input("Quantas escalas: "))
                        break

                    except:
                        print("Apenas números!!!")
                cidadeE = []
                if NumE >= 0:
                    for i in range(1,NumE+1):
                        cidE = input(f"Nome da {i}º cidade: ")
                        cidadeE.append(cidE)

                voos[cod] = [cidadeO,cidadeD,NumE,cidadeE]

                print("\nVOO CADASTRADO COM SUCESSO\n")

                controle2 = 1
                while controle2 == 1:

                    opc = input("Desenja cadastrar outro voo(s = sim | n = não): ")

                    if opc == 's' or opc == 'S':
                        print("\nProximo voo\n")
                        controle2 = 0
                        
                    elif opc == 'n' or opc == 'N':
                        controle2 = 0
                        controle = 0
                    else:
                        print("\n---Está opção não existe!---")

        elif menu == 2:

            if len(voos) != 0:
                print("\n|| ALTERAR INFO DO VOO ||\n")
                print('-=' * 66)
                print(f"| {'Codigo':^10} | {'Origem':^30} | {'Destino':^20} | {'Qunt. Escalas':^21} | {'Cid. Escalas':^35} |")
                print('-' * 132)
                for codV, voo in voos.items():
                    print(f'| {codV:^10} | {voo[0]:^30} | {voo[1]:^21}| {voo[2]:^22}| {str(voo[3]):^36}|')
                    print('-=' * 66)

                while True:
                    try:
                        print("\nQUAL VOO DESEJA ALTERAR? \n")
                        codE = int(input("Código do voo que deseja alterar: "))
    
                    except:
                        print("\nApenas números!!\n")

                    if codE in voos.keys():
                       
                        cidadeO = input("Cidade de origem: ")
                        cidadeD = input("Cidade de destino: ")
                        while True:
                            try:
                                NumE = int(input("Quantas escalas: "))
                                break

                            except:
                                print("Apenas números!!!")
                        cidadeE = []
                        if NumE >= 0:
                            for i in range(1,NumE+1):
                                cidE = input(f"Nome da {i}º cidade: ")
                                cidadeE.append(cidE)

                        for voov,alterar in voos.items():   
                            if  voov == codE:
                                alterar[0] = cidadeO
                                alterar[1] = cidadeD
                                alterar[2] = NumE
                                alterar[3] = cidadeE
                                print("\nALTERAÇÂO FEITA COM SUCESSO!!\n")
                        break
                    else:
                        print("\nEste voo não existe!!")

            else:
                print("\nNão ha nenhum voo cadastrado")

        elif menu == 3:

            if len(voos) != 0:

                print("\n|| EXCLUIR VOO ||\n")
                print('-=' * 47)
                print(f"| {'Codigo':^10} | {'Origem':^30} | {'Destino':^20} | {'Qunt. Escalas':^21} |")
                print('-' * 94)
                for codV, voo in voos.items():
                    print(f'| {codV:^10} | {voo[0]:^30} | {voo[1]:^21}| {voo[2]:^22}|')
                    print('-=' * 47)

                while True:
                    try:
                        print("\nQUAL VOO DESEJA EXCLUIR: \n")
                        codE = int(input("Código do voo: "))
    
                    except:
                        print("\nApenas números!!\n")

                    if codE in voos.keys():
                        voos.pop(codE)
                        print("VOO EXCLUIDO COM SUCESSO")
                        break
                    else:
                        print("\nEste voo não existe!!")

            else:
                print("\nNão ha nenhum voo cadastrado")

        elif menu == 4:
            
            if len(voos) != 0 :

                print("\n|| BUSCAR VOOS ||\n")
                
                while True:
                    
                    while True:
                        print("\n1.Buscar por cidade de origem\n2.Buscar ppor cidade de origem e destino\n3.Voltar\n")
                        try:
                            opc = int(input("Opção: "))
                            break

                        except:
                            print("Está opção não existe")
                    
                    if opc == 1:
                        while True:
                            nomeCO = input("Nome da cidade de origem: ")
                            N = 0
                            for codC, cid in voos.items():
                                if cid[0] == nomeCO:
                                    print("\n|| VOOS DISPONIVEIS ||\n")
                                    print('-=' * 66)
                                    print(f"| {'Codigo':^10} | {'Origem':^30} | {'Destino':^20} | {'Qunt. Escalas':^21} | {'Cid. Escalas':^35} |")
                                    print('-' * 132)
                                    print(f'| {codC:^10} | {cid[0]:^30} | {cid[1]:^21}| {cid[2]:^22}| {str(cid[3]):^36}|')
                                    print('-=' * 66)
                                    N = 1
                                elif cid[0] != nomeCO:
                                    if N == 1:
                                        None
                                    else:
                                        N = 0
                            if N == 0:
                                print("\nNenhum voo cadastrado nesta origem!!")
                            break

                    elif opc == 2:
                        while True:
                            nomeCO = input("Nome da cidade de origem: ")
                            nomeCD = input("Nome da cidade de destino: ")
                            listE = []
                           

                            N = 0
                            for cidn in voos.values():
                                    
                                if cidn[0] == nomeCO and cidn[1] == nomeCD:

                                    numM = cidn[2]
                                    listE.append(numM)

                                elif cidn[0] != nomeCO and cidn[1] != nomeCD:
                                    if N == 1:
                                        None
                                    else:
                                        N = 0
                            if N == 0:
                                print("\nNenhum voo cadastrado nesta origem!!")  
                            if len(listE) > 0:
                                for cid,cidn in voos.items():
                                        
                                        minE = min(listE)
                                        
                            
                                        if cidn[2] == minE:
                                            
                                            codigo = cid
                                        
                                            if cidn[0] == nomeCO and cidn[1] == nomeCD:
                                                if codigo in voos.keys():
                                                                td = voos[codigo]
                                                                print("\n|| VOO DISPONIVEIS COM A MENOR NUMEROD DE ESCALAS ||\n")
                                                                print('-=' * 66)
                                                                print(f"| {'Codigo':^10} | {'Origem':^30} | {'Destino':^20} | {'Qunt. Escalas':^21} | {'Cid. Escalas':^35} |")
                                                                print('-' * 132)
                                                                print(f'| {codigo:^10} | {td[0]:^30} | {td[1]:^21}| {td[2]:^22}| {str(td[3]):^36}|')
                                                                print('-=' * 66)                                                                          

                            break
                            
                    elif opc == 3:
                        break

            else:
                print("\nnão existe nenhum voo cadastrado")

        elif menu == 5:
            break

        else:
            print("\n---Está opção não existe!---")
                        
                        
        
                
        
  
