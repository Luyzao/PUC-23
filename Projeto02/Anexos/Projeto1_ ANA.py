#PRIMEIRO PASSO - ABRIR O CAIXA
print(f"\tBem-Vindo!!!")
password_correta = 1234
ten = 3

while ten > 0:
        
        password = int(input("Dígite sua senha para abrir o caixa: "))  

        if password != password_correta:

            if ten == 1:
                break
            
            else:
                ten -= 1

            print(f"VC TEM DIREITO A MAIS {ten} TENTATIVAS")  

        else:
            ten = 0
            print(f"Senha Correta \n Caixa Aberto!")

            break

#SEGUNDO PASSO - LEITURA DAS VENDAS
#o caixa recebe: R$1280 para o troco;

print("\n\n\tINSERCAO DOS ITENS VENDIDOS\n")
print("Para finalizar a compra digite '0' e em seguida 'SIM' ")
print("Para alterar o valor de um item digite '-1' \n\n")

#quantidade dos itens vendidos
item = 0
#soma total dos itens
soma_valor = 0
valor_item = 0
fim = "N"
fim_do_caixa = "N"


while fim == "N" or fim == "n" and fim_do_caixa == "N" or "n": #Não quero quero finalizar determinada venda E não quero fechar o caixa
    item += 1
    soma_valor+=valor_item
    valor_item = float(input(f"Digite o valor do item {item}: R$"))

    if valor_item < -1:
        soma_valor-=valor_item
        print ("Digite um valor valido!")

    elif valor_item == 0:
        ten_opc = 2                                    
        fim = input(f"Deseja Realmente Finalizar?? (S= Sim e N= Não)\n")
        #se digitar sim, o programa dá um break e irá para a terceira parte.
        if fim == "S" or fim =="s":
                item -= 1
                print(f"Venda Finalizada {item} itens")
                ten_opc = 0
                print("VENDA FINALIZADA")
                print(f"O valor total é: R$ {soma_valor:.2f}")
                valor_pago = float(input(f"Valor pago: R$ "))
                troco = valor_pago - soma_valor

                if troco == 0.00:
                    print(f"NÃO HÁ TROCO")
                elif troco == 200 or 100 or 50 or 5 or 2 or 1 or 0.5:
                    print(f"O valor do troco: R$ {troco:.2f} ")

        fim_do_caixa = input("Deseja fechar o caixa? (S = Sim e N = Não)\n")
        if fim_do_caixa == 'S' or fim_do_caixa == "s":
            print("Caixa fechado!")
            break
        else:
            item -= 1
    elif valor_item == -1:
        print(f"Escreva o valor correto do item {item}: R$")
        item -= 1
