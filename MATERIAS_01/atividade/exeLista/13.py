lista = []
N = int(input("ESCREVA QUANTOS NUMEROS QUER ESCRVER: "))

for i in range(N):
    num = int(input("ESCREVA UM NUMERO: "))
    lista.append(num)



for i in range(len(lista)):
    if lista[i] % (i+1) != 0:
        print(f"NUMERO PRIMO: {lista[i]}")
    else:
        print(f"NUMEROS NÃO PRIMOS: {lista[i]}")
