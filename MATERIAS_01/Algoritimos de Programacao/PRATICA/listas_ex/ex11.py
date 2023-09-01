#11. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
#quantos alunos com mais de 13 anos possuem altura inferior à média de altura
#desses alunos. Trabalhe com listas

alunos = 5
altura = 0
idade = 0
dados_alunos=[]
media_altura = 0
soma_altura=0
alunos_13=0


for aluno in range(1,alunos+1):
    
    altura = int(input(f"Insira a altura do aluno {aluno} "))
    idade = int(input(f"Insira a idade do aluno {aluno} "))
    dados_alunos.append(altura)
    dados_alunos.append(idade)
    soma_altura+=altura
    media_altura= soma_altura/alunos

    if alunos>13 and altura<media_altura:
        alunos_13+=1

print(f"Existem {alunos_13} alunos com 13 anos e abaixo da media de altura de {media_altura}")
