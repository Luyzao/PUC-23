#Construa um programa que seja cons#tuído de uma lista GAB de 10 elementos
#caracteres ( esta lista pode ser cons#tuída somente dos caracteres a, b, c, d e e. O
#programa irá ler o nome e a resposta de 10 alunos de uma turma e deverá imprimir
#a nota de cada aluno (considerando que cada questão vale 1,0 ponto). O programa
#deverá também imprimir a média da sala

GAB = ['a','b','c','d','e','a','b','c','d','e']
alunos = []
nota=0
soma=0
## entrada de dados
qtd_alunos=int(input("Digite a quantidade de alunos para correção: "))

for a in range(1,qtd_alunos+1):
    nome= str(input(f"Insira o nome do aluno {a}: ")).strip().upper()
    resp= str(input(f"Digite as respostas do aluno {a} (sem espaco): ")).strip().lower()
    #calculo nota
    nota=0
    for r in range(len(resp)): #transforma a resposta em lista
        if resp[r]==GAB[r]: #acessa o item da lista resp pelo indice r
            nota+=1

    
    alunos.append([nome, nota])

    
    #print(alunos) #lista toda com todos os elementos
    #print(alunos[0]) #lista a primeira sub lista  da lista 
    #print(alunos[0][1]) #lista o segundo elemento da primeira sub lista

## 
print("")
for aluno in alunos: #para o item 1 faça. trata o item 1 como uma lista normal
    print("Aluno:", aluno[0], "Nota: ",aluno[1]) 
    soma+=aluno[1]

## calculo da media

media = soma/qtd_alunos

print("A media da sala é: ",media)