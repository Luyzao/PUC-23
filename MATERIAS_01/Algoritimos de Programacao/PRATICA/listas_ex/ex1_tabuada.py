#Elabore um programa que imprima os resultados da tabuada de um número inserido pelo usuário.


num = int(input("\n\nDigite um numero para realizar a tabuada! "))
limite = int(input("Digite limite de parada "))

for i in range (0,limite+1):

    print(f" {num} x {i} = {num*i}")