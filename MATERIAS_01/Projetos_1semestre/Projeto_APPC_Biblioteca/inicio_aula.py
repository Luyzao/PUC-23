d_livros = {}

while True:
    try:
        codigo_livro = int(input("Digite o código do livro: "))
        titulo_livro = input("Digite o título do livro: ")
        n_autores = int(input("Digite o número de l_autores do livro: "))
        l_autores = []
        for i in range(n_autores):
            autor = input(f"Digite o nome do autor {i+1}: ")
            l_autores.append(autor)
        preco = float(input("Digite o preço do livro: "))
        d_livros[codigo_livro] = [titulo_livro, n_autores, l_autores, preco]
    except ValueError:
        print("Valor inválido. Tente novamente.")
    except:
        print("Erro inesperado. Tente novamente.")
    else:
        continuar = input("Deseja continuar cadastrando d_livros? (s/n): ")
        if continuar.lower() == "n":
            break

# Buscar livro pelo título
titulo_livro_busca = input("Digite o título do livro que deseja buscar: ")
encontrado = False
for livro in d_livros.values():
    if livro[0] == titulo_livro_busca:
        print(f"Resultado da busca pelo título '{titulo_livro_busca}':")
        print("Código:", list(d_livros.keys())[list(d_livros.values()).index(livro)])
        print("Título:", livro[0])
        print("Número de l_autores:", livro[1])
        print("Autores:", ", ".join(livro[2]))
        print("Preço:", livro[3])
        encontrado = True
if not encontrado:
    print(f"Livro com título '{titulo_livro_busca}' não encontrado.")

# Buscar livro pelo código
codigo_busca = int(input("Digite o código do livro que deseja buscar: "))
if codigo_busca in d_livros:
    print(f"Resultado da busca pelo código {codigo_busca}:")
    livro = d_livros[codigo_busca]
    print("Título:", livro[0])
    print("Número de l_autores:", livro[1])
    print("Autores:", ", ".join(livro[2]))
    print("Preço:", livro[3])
else:
    print(f"Livro com código {codigo_busca} não encontrado.")

# Imprimir dados dos d_livros com preço superior a R$50.00
print("Livros com preço superior a R$50.00:")
print("-" * 50)
print("| {:^10} | {:^30} | {:^20} |".format("Código", "Título", "Preço"))
print("-" * 50)
for codigo_livro, livro in d_livros.items():
    if livro[3] > 50.0:
        print("| {:^10} | {:^30} | {:^20.2f} |".format(codigo_livro, livro[0], livro[3]))
        print("-" * 50)
