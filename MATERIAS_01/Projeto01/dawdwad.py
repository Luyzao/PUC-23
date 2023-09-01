#LUIZ GUSTAVO PINTO DA SILVA RA:23013028

voos = {}

while True:
        
        print("\n1.Cadastrar novo voo\n2.Alterar info do voo\n3.Excluir voo\n4.Buscar voo\n")

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
                        break
                        
                    except:
                        print("\nApenas números!!!\n")
                
                while True:

                    if cod in voos.keys():
                        print("Este codigo já exite!!")
                    else:
                        break
                
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
                    else:
                        print("Está opção não existe!")
                    



        elif menu == 2:
            print("")


        elif menu == 3:
            print("")


        elif menu == 4:
            print("")


        elif menu == 5:
            print("")


        else:
            print("Está opção não existe")
                        
                        
        
                
        
  

