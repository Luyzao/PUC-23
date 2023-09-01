#Calculo de nota

#leitura das notas e pesos

n1=float(input("Digite o valor da nota 1: "))
p1=int(input("Digite o valor do PESO 1 em inteiro: "))
n2=float(input("Digite o valor da nota 2: "))
p2=int(input("Digite o valor do PESO da nota 1 em inteiro: "))

#Calculo de media

media=(p1*n1 + p2*n2)/(p1+p2)

print(f"\n\t O aluno teve como média a nota e {media:.1f} ")

if media==10:
    print("Aprovado com Distincao")
elif media >=7:
    print("APROVADO")
else : 
    print("Reprovadooooo")