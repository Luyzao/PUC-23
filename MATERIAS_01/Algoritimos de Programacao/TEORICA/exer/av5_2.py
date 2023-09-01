## entrada de dados

jogos = []
total=0

while True:
    try: 
        n = int(input("Quantos jogos deseja cadastrar? "))
        if n>0:
            break
        else:
            print("Digite somente numeros inteiros positivos!!")
    except:
        print("Digite somente numeros!")
for jogo in range(1,n+1):
    print(f'{f"Cadastro do Jogo {n}":^40}')
    nome = str(input('Digite o nome do jogo: ')).strip().upper()
    empresa = str(input('Digite o nome da empresa: ')).strip().upper()
    while True:
        try:
            ano = int(input("Digite o ano de lançamento: "))
            if ano>0:
                break
            else:
                print("Digite apenas numeros inteiros!")
        except:
            print("Digite apenas numeros!")
    tipo = str(input("Digite o tipo do jogo: "))
    jogos.append([nome,empresa,ano,tipo])

## pesquisa jogos

print(f'{f"Busca Sobre Jogo":^40}')
empresa_b = input("Insira a empresa: ").strip().upper()

while True:
    try: 
        ano_i = int(input("Insira o ano inicial de busca: "))
        ano_f = int(input("Insira o ano final de busca: "))
        if ano_i > 0 and ano_f>0:
            break
    except:
        print("Insira somente numeros inteiros positivos!")

## Percorrer lista
# 0 - nome 1 - empresa 2 - ano 3 - tipo 
for jogo in jogos:
    print("Jogos da Empresa", empresa_b)

    if jogo[1]==empresa_b and ano_i<=ano<=ano_f:
        print(f"{f'Nome do Jogo: {jogo[0]} Empresa: {jogo[1]} Ano: {jogo[2]} Tipo: {jogo[3]}'}")   
        total+=1 #contagem de jogos achados

    elif jogos==[]:
        print("Lista vazia!")
    else:
        print("Nao ha jogos nessas condições!")

if total>0:
    print("O numero total de jogos é: ",total)

