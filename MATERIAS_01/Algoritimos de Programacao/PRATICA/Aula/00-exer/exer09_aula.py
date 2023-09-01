###"""Construir um programa que faz a leitura de duas notas de um aluno, N1 e N2, e os respectivos 
##pesos, P1 e P2. O programa deve calcular a média ponderada alcançada por aluno e apresentar:A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
##A mensagem "Reprovado", se a média for menor do que sete;A mensagem "Aprovado com Distinção", se a média for igual a dez."""

a= float(input("Insira a primeira nota"))
b= float(input("Insira a segunda nota"))

#aprovado maior ou igual 7
#aprovado 10
#reprovado <7
media=(a+b)/2

if media==10:
    print(f"Aprovado com distincao! Nota {media}") 

elif media >=7:
    print(f"Aprovado")

else:
    print(f"Reprovado")


