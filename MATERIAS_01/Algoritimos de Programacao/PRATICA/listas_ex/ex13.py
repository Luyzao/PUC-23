#13. Os números primos possuem várias aplicações dentro da Computação, por exemplo
#na Criptograﬁa. Um número primo é aquele que é divisível apenas por um e por ele
#mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não
#um número primo

num = int(input("Digite um numero: "))


if num <=1:
    print("Não é primo")
else:
    for i in range(2,num):
        if num%i==0:
            print("Nao é primo")
            print(i)
            break

    else: print("é primo")


