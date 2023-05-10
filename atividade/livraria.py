tudoL = {}



quantL = int(input("Escreva a quantidade de livros que ira cadastrar: "))

for i in range(quantL):
    livros = {}
    codL = int(input("Codigo do livro: "))
    titulo = input("Título do livro: ")
    quntA = int(input("Quantidade de autores: "))

    for i in range(quntA):
        autores = []
        Nautores = input(f"Nome do {i}° autor: ")
        autores.append(Nautores)
    
    preco = float(input("Digite o valor do livro: "))
   
    livros = {'titulo':titulo,'quantidade_autores':quntA,'autores':autores,'preco':preco}

    tudoL[codL] = [livros]
 
   

while True:

    opc = int(input("Opções de pesquisa:\n1º Título do livro\n2º Codigo do livro"))

    if opc == 1:

        tituloL = input("Escreva o nome do livro desejado: ")

        if tituloL in livros.values():
            
            print("true")
            print(livros)
            

        else:
            print("Este livro não esta registrado")

    elif opc == 2:

        codigoL = int(input("Escreva o codigo do livro desejado: "))

        if codigoL in tudoL.keys():
            print("true")
            print(livros)
            # print(f"codigo: {livros[0]},Titulo: {livros[1]},Números de Autores: {livros[2]},Preço: {livros[3]}")
        
        else:
            print("Este livro não esta registrado")

    else:
        print("informção invalida tente novamente")
