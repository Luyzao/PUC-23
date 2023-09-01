lista = []
lista2 = []
for i in range(20):
    N = int(input("Escreva um numero: "))
    lista.append(N)

for i in range(len(lista)):
    if lista[i] % 3 == 0:
        lista2.append(lista[i])

print(f"Numeros multiplos de 3: \n{lista2}")


