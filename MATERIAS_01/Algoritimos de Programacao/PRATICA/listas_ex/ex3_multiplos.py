#Crie um algoritmo que receba do usuário um número qualquer e veriﬁque se esse é
#múlplo de 5 e 7


num = int(input("Insira um numero: "))

if num%5==0 and num%7==0:
    print("O numero multiplo de 5 e 7")
else:
    print("O numero nao e multiplo de 5 e 7")