#12. Faça um Programa que peça as duas notas de 10 alunos, calcule e armazene numa
#lista a média de cada aluno, imprima o número de alunos com média maior ou igual
#a 7.0.


alunos = 4
medias = []
nota1=0
nota2=0
media_aluno=0
alunos_7=0

for aluno in range(1,alunos+1):
    nota1=float(input(f"Digite a primeira nota1 {aluno}: "))
    nota2=float(input(f"Digite a segunda nota do aluno {aluno}: "))
    media_aluno = ((nota1+nota2)/2)
    medias.append(media_aluno)

for media in medias:
    if media >=7.0:
       alunos_7+=1

print(f"A quantidade de alunos que teve a media sete ou maior que sete foram {alunos_7}")
 