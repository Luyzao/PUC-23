#1. Construir um programa que faz a leitura de N produtos (código: inteiro, descrição: string, quantidade: inteiro, preço:
#real. Organizar os dados em um dicionário.
#Após o trecho da leitura dos dados dos N produtos, fazer a leitura de um determinado código de produto e buscar o
#produto com aquele código e, aumentar o preço do produto em 10%.
#Imprimir os dados desse produto, antes e depois de ter seu preço aumentado.
#Caso o código lido não exista, imprimir mensagem de que o código é inválido e, nesse caso, não precisa repetir a leitura,
#pode encerrar o programa

##Entradas

produtos={}

while True:
    try:
        N=int(input("Digite quantos produtos quer adicionar: "))
        if N>0:
            break
    except:
        print("Insira somente numeros validos!")

for n in range(1,N+1):

    codigo=int(input("Insira um codigo: "))
    if codigo in produtos.keys():
        print("Chave ja existente!")
    else:
        descricao=input("Digite a descricao do produto: ")
        quantidade=int(input("Insira a quantidade: "))
        preco =float(input("Insira o preco do item: "))
        produtos[codigo]=[descricao,quantidade,preco]
        print(produtos)

## Busca pelo produtos
busca=int(input("Digite o codigo "))


'''busca = int(input("Digite o codigo a ser buscado: "))

if busca in produtos.keys():
    produto = produtos[busca]
    preco_antigo = produto[2]
    preco_novo = preco_antigo * 1.10
    print(f"Codigo {busca} Produto: {produto[0]} Preco: {preco_antigo}")
    print(f"Codigo {busca} Produto: {produto[0]} Preco: {preco_novo}")
    produtos[busca][2]=preco_novo

else:
    print("Chave nao existe!")'''

