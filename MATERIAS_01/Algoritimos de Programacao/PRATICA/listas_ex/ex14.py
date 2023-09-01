#14. Elabore que leia vários números, até o usuário digitar 0. O programa deverá imprimir,
#quantos números foram lidos, qual é o maior e o segundo maior número lido

controle = 1
num = 0
num_lidos=0
maior=0
maior2=0
temp=0 
while controle>0:

    num=int(input("Digite um numero:"))

    num_lidos+=1

    if maior<num:
        temp=maior
        maior=num

        if maior>maior2:
            maior2=temp

    if num == 0:
        num_lidos-=1
        break

print(f"Foram lidos {num_lidos} numeros")
print(f"O maior foi {maior} e o segundo maior foi {maior2}")
