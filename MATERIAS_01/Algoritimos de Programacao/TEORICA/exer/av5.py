#Construir um programa que faz a leitura de N dados de cadastro de games contendo: nome do jogo (string), empresa (string), ano de
#lançamento (int) e tipo(string). Os dados dos games devem ser, obrigatoriamente, armazenados numa estrutura de lista, com sublistas,
#como no exemplo dado em classe. 
#Após o trecho da leitura dos dados dos N games e a montagem da lista, fazer a leitura de uma
#determinada empresa e de um período: ano_inicio e ano_final e, o programa, deve imprimir os dados (TODOS OS CAMPOS) dos games que
#atendam os valores lidos: empresa e ano de lançamento dentro do período. Além disso, no final, deverá imprimir o total de games nestas
#condições. Verificar se a lista está vazia e, se estiver vazia, imprimir mensagem. O valor de N deve ser lido e maior do que zero - valide.
#Repita a leitura de N até que seja lido um valor maior ou igual a zero. Não utilizar método ou função pronta de lista para a solução do
#problema, com exceção de append e len, se necessário. Seu programa deve demonstrar seu conhecimento de percorrer elementos de uma
#lista.

## Entrada de dados

jogos=[]
total = 0

while True: 
    try:
        n_jogos = int(input("Numero de jogos a serem cadastrados: "))
        if n_jogos>0:
            break
        else:
            print("Insira somente numeros positivos!")
    except ValueError:
        print("Insira somente numeros inteiros!")
        

for n in range(1, n_jogos+1):
    print(f'{f"Cadastro Jogo nº {n}":^20}')
    jogo= str(input("Digite o nome do jogo: ")).strip().upper()
    empresa= str(input("Digite o nome da empresa do jogo: ")).strip().upper()
    
    while True:
        try:
            ano_lancamento=int(input("Digite o ano de lançamento: "))
            if ano_lancamento>0:
                break
            else:
                print("Insira somente numeros inteiros positivos")
        except:
            print("Insira somente numeros!")

    tipo= str(input("Digite o tipo do jogo: ")).strip().upper()
    jogos.append([jogo,empresa,ano_lancamento,tipo])

## informacoes para busca
print("Busca Por Jogos!")
empresa_busca = str(input("Insira a empresa: ")).strip().upper()
while True:
    try:
        ano_inicio = int(input("Insira o ano de inicio para busca: "))
        ano_final = int(input("Insira o ano final para busca: "))
        if ano_final >0  and ano_inicio>0:
            break
        else:
            print("Insira somente numeros positivos!!")
    except:
        print("Insira somente numeros inteiros")

## percorrer uma lista
print(f"Jogos da empresa {empresa_busca} no periodo de {ano_inicio} a {ano_final}")

for jogo in jogos: #para um elemnto na lista 

    if jogo[1] == empresa_busca and ano_inicio<=jogo[2]<=ano_final: #verifique se o primeiro item é igual
        print(f"Nome do jogo: {jogo[0]} \n Empresa: {jogo[1]} \n Ano de Lançamento: {jogo[2]}")
        total+=1
        print('-'*20)

if total>0: 
    print(f"\nTotal de Jogos: {total}")
else:
    print("\nNão ha jogos nessa condição")



