biblioteca = {}

print("\t---LIVRARIA DO LUIZ---")

quant = 1

while quant > 0:
    livros = {}

    print("\n\tInserindo um novo livro\n")
    
    cod = int(input("Código do livro: "))

    if cod in livros.keys():

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

        livros = {'titulo':title,'quantidade_autores':quntA,'autores':autores,'preco':preco}

        biblioteca[cod] = [livros]

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

    opc = input("Procura livro por código(c)\nProcura livro por titulo(t)\nDigite a opção: ")

    if opc == "c" or opc == "C":

        codBusca = int(input("Qual é o código do livro: "))

        if codBusca in biblioteca.keys():
            print(biblioteca.get(codBusca))
        else:
            print("este livro não está cadastradado")
    
    elif opc == "t" or opc == "T":

        titleBusca = input("Qual é o título do livro: ")


        
        if titleBusca in livros.values():
                print(dict.values(biblioteca))
                
            
        

    else:
        print("Está opção não exite!")
