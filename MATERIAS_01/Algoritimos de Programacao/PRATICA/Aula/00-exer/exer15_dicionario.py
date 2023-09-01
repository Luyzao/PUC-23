#Cadastro de aluno
#dados: ra nome e nota de n alunos
# é a chave
alunos = {}

while True:
    try:
        N = int(input("Digite o numero de alunos a serem cadastrados: "))
        if N>0:
            break
    except:
        print("Insira somente numeros! Positivos! ")

##entrada de dados
for n in range(1,N+1):
    while True:
        try:
            ra=int(input("Digite o numero do ra: "))
            if ra not in  alunos.keys():
                break
            else:
                print("Ja existe!")
        except:
            print("somente numeros!")
    nome = input("Insira o nome: ")
    nota = float(input("Insira o valor da nota: "))
    alunos[ra]=[nome,nota]

##saida de dados

print("Alunos e Notas")

for ra, dados in alunos.items():
    print(f"RA: {ra} NOME: {dados[0]} NOTA: {dados[1]} ")
    if dados[1]>5:
        print("Aprovado\n")
    else:
        print("Reprovado")
