#Construir um programa que faz a leitura de N dados de cadastro de uma imobiliária - tipo do imóvel (string), tamanho em metros
#quadrados (real), número de cômodos (inteiro), preço (real). Os dados dos imóveis devem ser, obrigatoriamente, armazenados numa
#estrutura de lista, com sublistas, como no exemplo dado em classe. Após o trecho da leitura dos dados dos N imóveis e a montagem da
#lista, fazer a leitura de um determinado tipo de imóvel e de uma faixa de valor: valor_mínimo e valor_máximo e, o programa, deve imprimir
#os dados (TODOS OS CAMPOS) dos imóveis que atendam os valores lidos: tipo do imóvel e preço dentro da faixa. Além disso, no final,
#deverá imprimir o total de imóveis nestas condições. Verificar se a lista está vazia e, se estiver vazia, imprimir mensagem. O valor de N deve
#ser lido e maior do que zero - valide. Repita a leitura de N até que seja lido um valor maior ou igual a zero. Não utilizar método ou função
#pronta de lista para a solução do problema, com exceção de append e len, se necessário. Seu programa deve demonstrar seu conhecimento
#de percorrer elementos de uma lista.

## ENTRADA DE DADOS

casas= []
total = 0

while True:
    try:
        n = int(input("Digite o numero de imoveis a serem cadastrados: "))
        if n>0:
            break
    except:
        print("Digite somente numeros positivos inteiros!!")


for n in range(1,n+1):
    print(f"Digite os dados do imovel nº {n}")
    tipo_imovel = str(input("Digite o tipo do imovel: ")).strip().upper()
    tamanho = float(input("Digite o tamanho em metros quadrados: "))
    n_comodos = int(input("Insira o numero de comodos: "))
    preco = float(input("Digite o valor do imovel: "))
    casas.append([tipo_imovel,tamanho,n_comodos,preco])

## Busca 
print("\nBusca por Imoveis ")
tipo_b = str(input("Digite o tipo de imovel a ser buscado: ")).strip().upper()
valor_min= float(input("Digite o valor minimo para busca: "))
valor_max = float(input("Digite o valor maximo para busca: "))

## percorrendo lista

for casa in casas:
    if casa[0]==tipo_b and valor_min<preco<valor_max:
        print("Imoveis encontrados!")
        print(f'{f"Tipo {casa[0]}, Tamanho {casa[1]}, Comodos {casa[2]}, Valor {casa[3]}"}')
        total+=1
    elif casas==[]:
        print("Sem imoveis cadastrados!")
    else:
        print("Nao ha casas nestas condições")
