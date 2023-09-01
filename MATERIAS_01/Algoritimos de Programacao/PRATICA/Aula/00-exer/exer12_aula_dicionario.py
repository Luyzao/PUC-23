N = int(input("Insira o numero de alunos: "))

d_alunos = {}

## adionar em dicionario 

for n in range(N):
    ra = int(input("Insira o ra do aluno: "))
    if ra in d_alunos.keys():
        print("RA ja existente")
        print("")
    else:
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        d_alunos[ra]=[nome,nota]

## imprimir tabela de alunos

for ra, dados in d_alunos.items():
    print(f'RA: {ra} | NOME: {dados[0]} | NOTA: {dados[1]} |', end=' ') ##tratar como lista dado
    if dados[1]>=5: 
        print("Aprovado")
    else:
        print("Reprovado")
