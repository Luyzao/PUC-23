#leitura de quantidade de nota que serao digitadas

while True:
    N = int(input("Numero de notas, Maior do que zero: "))

    if N>0:
        break
    else: print("Quantidade de Notas Invalida")

#iniciando a variavel que acumulara as somas com zero

soma=0
NOTAS = [] #iniciar lista vazia

for i in range(N):
    nota=float(input("Nota "))
    NOTAS.append(nota) #adição de elementos em lista
    soma+=nota

Media = soma/N

print(f'\nMedia da Classe {Media}')

print('Lista de Notas')

## percorrer elementos em lista

for nota in NOTAS:
    print(f'Nota: {nota:.1f}')