livros={
    123:['Pequeno Principe',1,['Fulaninho'],21.0], 
    321:['Eu sou o numero 4',2,['Albertinho'],54.01]
} 


## Funçao items

codigo = 321
busca_titulo = 'Pequeno Principe'

for cod, livro in livros.items():
    if busca_titulo==livro[0]:
        print('Cod: ',cod)
        print('Titulo:',livro[0])

for livro in livros.values():
    if busca_titulo==livro[0]:
        print(livro[3])
        print(f"{f'OLAAAA':^150}")






'''if codigo in livros.keys(): ##busca por chave com if e busca como lista

    livro = livros[codigo]
    print(f"Codigo {codigo} livro: {livro[0]} Autores: {livro[1]}")
    print(f"Codigo {codigo} livro: {livro[0]} Autores: {livro[1]}")'''




'''for codigo, item in livros.items():      ##Retorna todos os dicionarios 
    print(f"Livro:",item[0])
    print(f"Quantidade de autores: ",item[1])
    print(f'Autor: ',item[2])
    print(f'Preco: ', item[3])'''

'''for codigo in livros.values():          ##retornar todos os dicionarios --'
    print(f"Livro:",codigo[0])
    print(f"Quantidade de autores: ",codigo[1])
    print(f'Autor: ',codigo[2])
    print(f'Preco: ', codigo[3])    '''


'''if codigo in livros.keys(): ##Busca por codigo retorno de item
    liv = livros[codigo]
    print('tatan: ', liv[0])'''


