#Aula_01

nome="Ana Maria"
idade=30
peso=49.52

#print("\nNome=", nome, "Idade=", idade, "anos e peso =",peso, "Kg")
#print("\nNome=",nome,"\nIdade=",idade,"anos e \nPeso=",peso,"Kg\n")


print(f"\nNome: {nome} \tIdade: {idade} anos  \tPeso: {peso}Kg\n")
print(f"\nNome: {nome:^5} \tIdade: {idade:^3} anos \tPeso: {peso:^.2f}kg \n")
#####essa questao de {: ^3} funciona como


# Mostrar numero
print("<<<<<Entrada de Dados>>>>>>")
a=int(input("Digite um numero INTEIRO: "))
print(f"O numero digitado é: {a}")


# Efetuando operacoes

print("<<<<<APLICACOES MATEMATICAS>>>>>")

a=int(input("Insira um numero:"))
soma=a+1
subtracao = a - 1
multiplicacao = a* 1 
divisao = a / 2
resto = a//3
potencia = a**2

print(f"Soma {soma} \n subtracao {subtracao} \n multiplicacao {multiplicacao} \n divisao {divisao:.4f} \n resto {resto} \n potencia {potencia}")



