# Programa que faz leitura de 2 numeros inteitros e identifica qual : maior menor igual

a=int(input("Digite o primeiro numero inteiro "))
b=int(input("Digite o segundo numero inteiro "))


#Calculo

if a==b:
    print(f" Os numeros digitados sao iguais {a} = {b}")
elif a>b:
    print(f'O primeiro numero digitado é maior que o segundo {a} > {b}')
else:
    print(f'O segundo numero é maior que o primeiro {b} > {a}')
