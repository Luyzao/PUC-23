#Primeiro Passo - Abrir o caixa

senha = 1234

print ("\n\n\t\t Bem-vindo !! \t\t\n\n")
t=3
while t>0:
    t-=1
    senha2 = int(input("Digite sua senha para abrir o caixa: "))
    if senha2!=senha:
        print("Senha Incorreta!")
        print(f"Você tem direito a mais {t} tentativas")
        if t==0:
            print('Sistema deve ser Reinicializado')
    else:
        print("Senha Correta!!")
        print("Caixa Aberto!!")
        break

