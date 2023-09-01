#Ao usar range(len(lista)), estamos criando um objeto de intervalo com base no comprimento da lista. Esse objeto de intervalo vai gerar uma sequência de números que serão usados como índices 
#para acessar os elementos da lista.


lista = [1,2,3,4,5,6]



print("Lista Indice Impares: ", end='')
#A. imprimir os elementos que estao nas posicoes impares
for l in range(len(lista)):
    if l % 2 !=0: #divisao nao exata
        print(lista[l],end=' ')


#b. Construir uma nova lista com os elementos pares desta lista

l_pares=[]
print("\nLista Elementos Pares: ", end=' ')
for l in range(len(lista)):
    if lista[l] %2==0:
        l_pares.append(lista[l])

for l in l_pares:
    print(l, end=' ' )
print('\n')