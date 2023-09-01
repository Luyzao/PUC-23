#Construa um programa que seja cons#tuído de uma lista GAB de 10 elementos
#caracteres ( esta lista pode ser cons#tuída somente dos caracteres a, b, c, d e e. O
#programa irá ler o nome e a resposta de 10 alunos de uma turma e deverá imprimir
#a nota de cada aluno (considerando que cada questão vale 1,0 ponto). O programa
#deverá também imprimir a média da sala

#Variaveis 
GAB = ['a','b','c','d','e']
alunos = []
soma = 0
nota = 0 

# entrada de variaveis

cadastro = int(input("Digite o numero de alunos: "))

for c in range(cadastro):
    print(f"Insira os dados do {c}º aluno")
    nome = input("Insira o nome do aluno: ")
    respostas= str(input("Insira as respostas:"))

    for resp in range(len(respostas)): #LEN " TRANSFORMA STRING EM LISTA"
        if respostas[resp]==GAB[resp]: #se o elemento da lista 1 for igual o elemento da mesma posiçao em lista 2 
            nota+=1
