#Escreva um programa que imprima na tela os dez primeiros múltiplos de um
#número inteiro qualquer fornecido pelo usuário. No final, imprima também a soma
#destes dez números.

## entrada de dados

numero = int(input("Insira um numero inteiro: "))
soma = 0
multiplo = 1

# processamento

print("Lista de multiplos: ", end='')
for n in range(1,11):
    multiplo =numero*n
    soma+=multiplo
    print(n, end=',')

print("\nSOMA:", soma)