#17. Elabore uma lista em Python contendo 20 elementos. O programa deverá:
#a. imprimir os elementos que estão nas posições ímpares
#b. Construir uma nova lista com os elementos pares desta lista
#c. Imprimir o maior e o menor elemento desta lista

import random

# Cria uma lista aleatória com 20 elementos
lista = [1,2,3,4,5,6,7,8]

# a) Imprime os elementos das posições ímpares
print("Elementos das posições ímpares:")
for i in range(len(lista)):
    if i % 2 == 1:
        print(lista[i],end=' ')

# b) Cria uma nova lista com os elementos pares da lista original
lista_pares = [num for num in lista if num % 2 == 0]
print('\n',lista_pares)
# c) Imprime o maior e o menor elemento da lista original
maior = max(lista)
menor = min(lista)
print("Maior elemento:", maior)
print("Menor elemento:", menor)
