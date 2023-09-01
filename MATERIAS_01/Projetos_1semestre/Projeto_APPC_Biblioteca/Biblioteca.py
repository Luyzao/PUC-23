#Ferramentas

d_livros={}
l_autores=[]
print('-'*80)
print('\n\t\t\t    Sistema de Livraria\n')
print('-'*80)


#Sistema de cadastro e Sistema de busca
while True:

    while True:
        try:
            
            escolha_sistema = int(input("Escolha entre as opcoes abaixo:\n 1 - Cadastrar livros \n 2 - Buscar livros \n 3 - Sair \n Digite a opção escolhida: "))
            break
        except ValueError:
            print("\n\nDigite somente numeros!\n\n")

    if escolha_sistema<1 or escolha_sistema>3:
        print("\nEscolha um opçaõ valida!\n") 
    else:
        break
           
# Escolha do sistema 

contador = 0

while 1<=escolha_sistema<=3:

    ##Sai do sistema 
  
    if escolha_sistema ==3:
        print('-'*80)
        print("\t\t\t    Volte sempre!")
        print('-'*80)
        break

    #Sistema de Castro
    if escolha_sistema ==1:
        print('-'*80)
        print("\n\t\t\t    Sistema de Cadastro\n")
        print('-'*80)
        deseja_continuar=1
        

        while deseja_continuar==1:
            contador+=1

            #Entrada e validacao codigo_livro
            while True: 
                try:
                    codigo_livro= int(input(f"\nDigite o codigo do livro {contador}: "))
                    break

                except ValueError:
                    print("Digite uma entrada valida! Apenas numeros inteiros")

            ##Busca do codigo para ver se o mesmo já existe
            if codigo_livro in d_livros.keys():
                print(f"Codigo ja existente! Pertence a outro livro")
                codigo_livro= int(input(f"Digite novamente o codigo do livro {contador}: "))

            #Entrada nome do livro
            titulo_livro = input(f"Digite o nome do livro {contador}: ").upper()

            #Entrada numero de autores
            while True:
                try:
                    n_autores = int(input(f"Digite o numero de autores do livro {contador}: "))
                    break

                except ValueError:
                    print("Digite apenas numeros!")
            
            for autor in range(1,n_autores+1):
                autor=input(f"Digite nome do {autor}º autor do livro {contador}: ").upper()
                l_autores.append(autor)
            
            #Preco
            while True:
                try:
                    preco_livro= float(input(f"Insira o valor do preco do livro {contador} R$: "))
                    break
                except ValueError:
                    print("Digite apenas numeros! Ex: 15.50")


            #Conferencia de informacoes

            while True:
                try:
                    print('-'*80)
                    print(f"Informacoes adicionadas: \n 1- Codio Livro: {codigo_livro} \n 2- Titulo: {titulo_livro} \n 3- Numero de Autores: {n_autores} \n 4- Nome Autores: {l_autores} \n 5 -Preco: {preco_livro}")
                    print('-'*80)
                    conf_informacoes = int(input(f"As informações estao corretas? [1-SIM] ou [2-NAO]: "))
                   
                    if conf_informacoes == 1:
                        break
                    elif conf_informacoes > 6 or conf_informacoes< 1:
                        print("Escolha uma opçao valida!")
                    else:
                        print('')
                        print('-'*20,'Alteracao','-'*20)
                        print('')
                        n_alteracao = int(input("Escolha o item para ser alterada ou [6]- Para sair : "))
                        if n_alteracao==6:
                            break
                        elif n_alteracao ==1:
                            codigo_livro=int(input("Insira o codigo do livro correto: "))
                        elif n_alteracao ==2:
                            titulo_livro= input("Digite o titulo correto do livro: ").upper
                        elif n_alteracao ==3:
                            n_autores = int(input("Digite o numero de autores correto: "))
                        elif n_alteracao==4:
                            for autor in range(1,n_autores+1):
                                autor=input(f"Digite nome do {autor}º autor: ").upper()
                                l_autores.append(autor)
                        elif n_alteracao ==5:
                            preco_livro= float(input(f"Insira o preco do livro {contador}, correto: R$ "))

                except ValueError:
                    print("Insira apenas numeros inteiros!")
            
             #Adicao dicionario
            d_livros[codigo_livro]=[titulo_livro,n_autores,l_autores,preco_livro]
            
            print(f"\n\tLivro adicionado com sucesso! {d_livros}\n")
            print('-'*80)
            
            #Continuacao Cadastro

            deseja_continuar=int(input("\n\nDeseja inserir outro livro?: [1-Sim / 2-Nao ]: "))
            
            if deseja_continuar==2:
                while True:
                    while True:
                        try:
                            escolha_sistema = int(input("Escolha entre as opcoes abaixo:\n 1 - Cadastrar livros \n 2 - Buscar livros \n 3 - Sair \n Digite a opção escolhida: "))
                            break
                        except ValueError:
                            print("\n\nDigite somente numeros!\n\n")

                    if escolha_sistema<1 or escolha_sistema>3:
                        print("\nEscolha uma opçaõ valida!\n") 
                    else:
                        break
            else:
                print("Insira os dados para o proximo livro: ")
            
     #Sistema de Busca

    if escolha_sistema==2:
        print('-'*70)
        print("\n\t\t\t    Sistema de Busca! ")
        print('-'*70)
        print(f"Livros cadastrados no Sistema {contador}\n")

        #Escolha do tipo de busca desejado

        while True:

            while True:
                try:
                    busca=int(input(f"Deseja buscar por: [1]- Titulo [2]- Codigo [3]- Busca por valores acima de 50 reais [4]- Retornar [5] - Menu principal: "))
                    break
                except ValueError:
                    print("Digite apenas numeros!")
            if busca<1 or busca>4:
                print("Escolha uma opcao valida!")

            #Buscar pelo titulo
            elif busca==1:         
                busca_titulo=input("Digite o nome do livro para busca: ").upper()


                for codigo_livro, dados_livros in d_livros.items():

                    if dados_livros[0]==busca_titulo:
                        print("-"*70)
                        print(f"Resultado da busca pelo titulo '{dados_livros[0]}:")
                        print(f"Codigo do livro: {codigo_livro} ")
                        print(f"Autores: {l_autores}")
                        print(f"Preco: R$ {preco_livro}")
                        print('-'*70)


            #Buscar pelo codigo
            elif busca==2:
                busca_codigo=int(input("Digite o codigo do livro para busca: "))

                for codigo_livro in d_livros.keys():
                    if codigo_livro==busca_codigo:
                        print("-"*70)
                        print(f"Codigo do livro: {codigo_livro}")
                        print(f"Titulo do livro: {titulo_livro}")
                        print(f"Autores: {l_autores}")
                        print(f"Preco: R$ {preco_livro}")
                        print("-"*70)

            #Buscar pelo valor
            elif busca==3:

                print("Livros com preço superior a R$50.00:")
                print("-" * 70)
                print(f"| {'Codigo':^10} | {'Titulo':^30} | {'Preço':^20} |")
                print("-" * 70)
                print
                for codigo_livro, dados_livros in d_livros.items():
                    if dados_livros[3] >= 50: #d_livros[1][3]
                        print(f"| {codigo_livro:^10} | {titulo_livro:^30} | {preco_livro:^20.2f} |")

                        print("-" * 70)
            elif busca==4:
                break






                        



                





