#17. Elabore uma lista em Python contendo 20 elementos. O programa deverá:
#a. imprimir os elementos que estão nas posições ímpares
#b. Construir uma nova lista com os elementos pares desta lista
#c. Imprimir o maior e o menor elemento desta lista

# Lista GAB com as respostas corretas
GAB = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']

# Lista para armazenar o nome e a nota de cada aluno
notas = []

# Loop para ler o nome e a resposta de cada aluno
for i in range(2):
    nome = input("Digite o nome do aluno {}: ".format(i+1))
    resposta = input("Digite as respostas do aluno {} (sem espaço): ".format(i+1))

    # Compara a resposta do aluno com o GAB e calcula a nota
    nota = 0
    for j in range(len(resposta)):
        if resposta[j] == GAB[j]:
            
            nota += 1

    # Armazena o nome e a nota do aluno na lista de notas
    notas.append((nome, nota))

# Imprime a nota de cada aluno
print("\nNotas dos alunos:")
for nome, nota in notas:
    print("{}: {}".format(nome, nota))

# Calcula e imprime a média da sala
media = sum(nota for nome, nota in notas) / len(notas)
print("\nMédia da sala: {:.2f}".format(media))
print(len(notas))