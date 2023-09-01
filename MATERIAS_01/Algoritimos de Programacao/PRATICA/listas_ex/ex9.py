#9. Elabore um programa que leia um conjunto de vários valores inteiros e os coloque
#em 2 listas conforme forem pares ou ímpares (uma lista para números pares e outra
#lista para números ímpares). A leitura dos números é ﬁnalizada quando um número
#negativo é lido.

print("Insira um numero negativo para parar")

lista_par= []
lista_impar=[]
num =0

while num>=0: 
    num = int(input("Insira um numero: "))

    if num%2==0 and num>0:
        lista_par.append(num)

    elif num%2!=0 and num>0:

        lista_impar.append(num)
    elif num <0:
        break


for num in lista_par:
    print(f"Elementos lista par {num}")

for num in lista_impar:

    print(f"Elementos lista impar {num}")


