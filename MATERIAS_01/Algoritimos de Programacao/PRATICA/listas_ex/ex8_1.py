#8. Elabore um programa que leia uma lista de no máximo 20 elementos inteiros. Em seguida o programa deverá imprimir a quan#dade de valores múltiplos de 3.

lista=[]
lista2=[]

while True:
    print("Insira no maximo 20 elemento!")
    elementos = int(input("Digite a quantidade de numeros a serem lidos: "))

    if elementos<20:
        break
    else:
        print("Insira um numero valido!")

for i in range (elementos):
    
    elemento=(int(input(f"Digite o numero {i} da lista:")))
    lista.append(elemento)

#Acomodacao em lista 

for elemento in lista:
    if elemento%3==0:
        lista2.append(elemento)


print(f"Elemento multiplo de 3 {lista2}")
