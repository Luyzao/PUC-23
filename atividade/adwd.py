biblioteca = {}

print("\t---LIVRARIA DO LUIZ---")

while True:
    print("\n\tInserindo um novo livro\n")
    cod = int(input("Código do livro: "))

    if cod in biblioteca.keys():
        print("Este livro já existe.")
    else:
        title = input("Título do livro: ")

        while True:
            quntA = int(input("Quantidade de autores: "))
            if quntA <= 0:
                print("\tEste valor corresponde a nenhum autor, tente novamente!")
            else:
                break

        autores = []
        for i in range(1, quntA+1):
            Nauto = input(f"Nome do {i}° autor: ")
            autores.append(Nauto)

        preco = float(input("Digite o valor do livro: "))

        livro = {'titulo': title, 'quantidade_autores': quntA, 'autores': autores, 'preco': preco}
        biblioteca[cod] = livro

        opc = input("Quer cadastrar mais livros? (S ou s/N ou n)")
        if opc.lower() == "s":
            print("\n\tcontinuando...\n")
        elif opc.lower() == "n":
            break
        else:
            print("Esta opção não existe!")

while True:
    print("\n\t---BUSCANDO LIVRO---\n")
    opc = input("Procurar livro por código (c)\nProcurar livro por título (t)\nDigite a opção: ")

    if opc.lower() == "c":
        codBusca = int(input("Qual é o código do livro: "))
        if codBusca in biblioteca.keys():
            print(biblioteca.get(codBusca))
        else:
            print("Este livro não está cadastrado.")
    elif opc.lower() == "t":
        title
