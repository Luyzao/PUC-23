#PROBLEMA – NIVEL II: construir um programa que faz a leitura DO NOME e das notas de
#N alunos, armazenando-as numa lista. Calcula a média da classe e imprime: a média da
#classe e o NOME e a NOTA apenas dos alunos com nota maior ou igual à média da classe

## variaveis 
lista=[] #com sublista
lista2=[] #sem sublista
soma = 0

## entradas

while True:
    try:
        N = int(input("Insira a quantidade de alunos: "))
        if N>0:
            break
        else:
            print("Somente numero positivos!")
    except ValueError:
        print("Insira somente numeros!")

for n in range(1,N+1):
    nome = input(f"Insira o nome do aluno {n}º: ")
    nota = float(input(f"Insira a nota do aluno {n}º: "))
    soma+=nota
    lista.append([nome,nota])
    lista2.append(nome)
    lista2.append(nota)


## processamento e saida
media = N/soma
print(f"A media da sala foi: {media}")

#Lista com sublista  saida de dados 
print("\nLista com sublista: alunos e notas: ",end='\n')
for dado in lista:
    print(f"Aluno: {dado[0]} Nota: {dado[1]}")


#lista sem sublistas saida de dados

print("\nLista sem sublista: ",end='')
for dado in range(0,(len(lista2)),2):
    
    print(f"\nNome: {lista2[dado]} e Nota: {lista2[dado+1]} ")


##saida