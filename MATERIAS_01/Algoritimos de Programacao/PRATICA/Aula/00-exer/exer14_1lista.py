#PROBLEMA – NIVEL II: construir um programa que faz a leitura DO NOME e das notas de
#N alunos, armazenando-as numa lista. Calcula a média da classe e imprime: a média da
#classe e o NOME e a NOTA apenas dos alunos com nota maior ou igual à média da classe


##entradas

lista=[]
soma = 0

while True:
    try:
        N= int(input("Digite o numero de alunos: "))
        if N>0:
            break
    except:
        print("Insira um valor valido!")

for n in range(1,N+1):
    nome = input(f"Digite o nome do {n}º aluno:")
    nota = float(input(f"Insira a nota do {n}º aluno: "))
    lista.append(nome)
    lista.append(nota)

for l in range(0,len(lista),2): # l é igual ao indice 
    print(f"NOME: {lista[l]} NOTA: {lista[l+1]}")