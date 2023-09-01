#10. Faça um Programa que leia uma lista de 10 números inteiros, mostre a soma, a
#multiplicação e os números.

lista = [] 
num = 0
soma = 0
multiplicacao=1
controle = 1
while controle <= 10:
    num=(int(input(f"Digite o numero {controle} ")))
    lista.append(num)
    controle+=1


for num in lista:
    soma+=num

for num in lista:
    multiplicacao*=num


print(f"Soma: {soma}")
print(f"Multiplicacao {multiplicacao}")
print("Numeros")

for num in lista:
    print(num,end=',')