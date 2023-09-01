#Escreva um algoritmo que leia n de números inseridos pelo usuário (n é fornecido
#pelo usuário) e realize a soma dos números pares e conta quantos ímpares o usuário
#digitou. O resultado da soma dos pares e o número de ímpares digitados deverá ser
#impresso no ﬁnal.


soma = 0
impares=0

qtd = int(input("Insira a quantidade de numeros desejada: "))

for i in range (qtd):
    numero_desejado = int(input("Digite o numero desejado "))

    if numero_desejado %2==0:
        soma+=numero_desejado
        
    else:
        impares+=1

print(f"Resultado soma {soma} Resultado impares {impares}")