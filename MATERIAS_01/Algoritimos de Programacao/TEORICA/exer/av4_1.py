#Escreva um programa que imprima na tela os N primeiros múltiplos de 5,
#iniciando em 5. O valor de N deve ser lido e ser maior ou igual a 10. Validar e
#repetir a leitura até que um valor válido de N seja digitado. No final, imprima
#também a soma destes N números.
#Ex: Valor de N: 11
#Lista de Múltiplos: 5 10 15 20 25 30 35 40 45 50 55
#Soma = 330

## entrada de dados

n  = int(input("Digite a quantidade de multiplos a serem exibidos: "))

multiplos=1
soma = 0
print("Valor de N: ", n)
print('Lista De Multiplos: ',end='')
for i in range(1,n+1):
    multiplos= 5*i
    soma+=multiplos
    print(multiplos, end=' ')  #sintaxe interessante end=',')
print("\nSoma: ",soma)
