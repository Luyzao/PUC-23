biblioteca = {}

print("\t---LIVRARIA DO LUIZ---")

quant = 1

while quant > 0:
    livros = {}

    print("\n\tInserindo um novo livro\n")
    
    cod = int(input("Código do livro: "))

    if cod in biblioteca.keys():

        print("este livro já exite")
        

    else:

        title = input("Título do livro: ")

        while True:
            quntA = int(input("Qunatidade de autores: "))

            if quntA <= 0:

                print("\tEste valor corresponde a nenhum autor, tentei novamente!")

            else:
                break

        for i in range(1,quntA+1):

            autores = []
            Nauto = input(f"Nome do {i}° autor: ")
            autores.append(Nauto)

        preco = float(input("Digite o valor do livro: "))

        biblioteca[cod] = [title,quntA,autores,preco]
        print("\nLIVRO CADASTRADO COM SUCESSO!!!\n")

        opc = input("Quer cadastrar mais livros? (S ou s/N ou n)")

        if opc == "s" or opc == "S":
            print("\n\tcontinuando...\n")

        elif opc == "n" or opc == "N":
            quant = 0

        else:
            print("Esta opção não extite!")

quant = 1

while quant > 0:

    print("\n\t---BUSCANDO LIVRO---\n")

    opc = input("Procura livro por código(c)\nProcura livro por titulo(t)\nVer o livros com valor de R$50,00 para cima(p)\nSair.(s)\n\n\nDigite a opção: ")


    if opc == "c" or opc == "C":

        codBusca = int(input("\nQual é o código do livro: "))

        if codBusca in biblioteca.keys():
            livro = biblioteca[codBusca]
            print(f'Titulo: {livro[0]}')
            print(f'Codigo: {codBusca}')
            print(f'Numero de autores:{livro[1]}')
            print(f'Autores: {livro[2]}')
            print(f'Preco: {livro[3]}')

        else:
            print("este livro não está cadastradado")
    
    elif opc == "t" or opc == "T":

        titleBusca = input("\nQual é o título do livro: ")
        for livro in biblioteca.values():
            
            if livro[0] == titleBusca:
                print(f'Título: {livro[0]}')
                print(f'Codigo: {list(biblioteca.keys())[list(biblioteca.values()).index(livro)]}')
                print(f'Numero de autores: {livro[1]}')
                print(f'Autores:{livro[2]}')
                print(f'preco: {livro[3]}')
            
    elif opc == "p" or opc == "P":
        
            for codP, livro in biblioteca.items():
                if livro[3] >= 50:
                    print('-=' * 35)
                    print(f"| {'Codigo':^10} | {'Titulo':^30} | {'Preço':^20} |")
                    print('-' * 70)
                    print(f'| {codP:^10} | {livro[0]:^30} | {livro[3]:^20.2f}|')
                    print('-=' * 35)
                else:
                    print("Nenhum livro dastrado acima de R$50,00")

    elif opc == "s" or opc == "S":
        quant = 0

    else:
        print("Está opção não exite!")
