# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
# quantos alunos com mais de 13 anos possuem altura inferior à média de altura
# desses alunos. Trabalhe com listas

lista = []
media = 0
N=3

for i in range(N):
    idade = int(input("ESCREVA SUA IDADE: "))
    altura = float(input("ESCREVA SUA ALTURA: "))
    media += altura/N
    lista.append([idade,altura])

for i in range(len(lista)):

    if lista[i][1] < media and lista[i][0] > 13:
        print(f"IDADE: {lista[i][0]} \nALTURA: {lista[i][1]}")
