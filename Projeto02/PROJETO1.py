#Primeiro Passo - ABRIR O CAIXA

print("\n\n\t Bem-Vindo!!!\n\n")

senha = 1234
t=0

while t<3:
    t+=1
    senha2=(int(input("Digite sua senha para abrir o caixa: ")))
    if senha!=senha2:
        print("\n\tSENHA INCORRETA\n\n")

        if t==1:
            print("Voce tem mais DUAS tentativas...\n")
        elif t==2:
            print("Voce tem mais UMA tentativa...\n")
        else:
            print("Sistema tem que ser Reinicializado!!!\n")
    else: 
        print("Senha Correta!")
        print("Caixa Aberto!!")
        break

#Troco inicial 

#numero de notas
n_200 = 2
n_100 = 4
n_50 = 6
n_10 = 10
n_5 = 10
n_1 = 20
n_05 = 20

notas200 = 200 * n_200
notas100 = 100 * n_100
notas50 = 50 * n_50
notas10 = 10 * n_10
notas5 = 5 * n_5
notas1 = 1 * n_1
notas05 = 0.5 * n_05

#Segundo Passo - Leitura das Vendas

print("\n\n\tINSERCAO DOS ITENS VENDIDOS\n")
print("Para finalizar a compra digite '0' e em seguida 'SIM' ")
print("Para alterar o valor de um item digite '-1' \n\n")


#quantidade dos itens vendidos
item = 0
#soma total dos itens
soma_valor = 0
valor = 0
fim = "N"

#Insercao dos Itens Vendidos

while fim == "N" or fim =="n":
        
        item+=1

        soma_valor+= valor
        valor = float(input(f"Digite o valor do Item {item}: R$"))

        if valor == 0:
            fim = str(input("Deseja Realmente Finalizar?? (S=Sim e N=Nao): "))
            if fim == "S" or fim == "s":
                print(f"Venda Finalizada com {item} ")

        elif valor <-1:
            soma_valor-=valor
            print ("Digite um valor valido!")
        elif valor ==-1:
            soma_valor-=valor
            valor = float(input("Digite o valor correto do item anterior: R$"))

#TERCEIRO PASSO - Finalizacao da venda e calculo do troco


print (f"Valor total: {soma_valor:.2f}")
valor_pago = (float(input("Insira o valor pago: ")))

if valor_pago == soma_valor:
    print("Nao há troco!!")

elif valor_pago < soma_valor:
    print("Valor insuficiente!")

elif valor_pago>soma_valor:
    troco = valor_pago - soma_valor
    print(f"Troco: {troco:.2f} ")

#troco
#         



    





