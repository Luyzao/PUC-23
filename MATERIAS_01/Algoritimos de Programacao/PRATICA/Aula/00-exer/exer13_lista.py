#Construir um programa que faz a leitura das notas de N alunos. Calcula a média da classe e
#imprime a lista de notas e a média da classe


##  variaveis

notas=[]
soma =0
media =0
## entrada 

while True:
    try:
        n = int(input("Insira o numero de alunos: "))
        if n>0:
            break
        else:
            print("Insira somente numeros positivos")
    except:
        print("Insira somente numeros inteiros positivos! ")

for i in range(1,n+1):
    nota=float(input(f"Insira a nota {i}: "))
    notas.append(nota)
    soma+=nota

## media
media = soma/n

## saida

print(f"A media da classe é: {media}")
print("As notas dos alunos foram: ")

for nota in notas: #por um elemento na lista
    print(f"Nota: ",nota)



