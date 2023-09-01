#entrada 

n = int(input('Digite um numero inteiro: '))
soma=0
multiplo = 1
print("Lista de Multiplos: ",end='')

for i in range(1,11):
    multiplo = n*i # multiplicaçao
    soma+=multiplo
    print(multiplo, end=' ')
print("\nSoma = ",soma)
