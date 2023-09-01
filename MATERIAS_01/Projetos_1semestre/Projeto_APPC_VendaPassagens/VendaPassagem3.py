#ANA CAROLINA MORELLI CHAVES 23017617
#CICERA EDUARDA DA COSTA 23016727
#LUIZ GUSTAVO PINTO DA SILVA 23013028

# Venda de Passagens Aéreas

# Armazenamento de informações
d_voo = {}


def exibir_menu():
    print("-" * 80)
    print(f'{"Seja bem-vindo!":^80}')
    print("-" * 80)
    print("[1] - Área Cliente")
    print("[2] - Área Colaborador")
    print("[3] - Sair do Programa")


def exibir_menu_colaborador():
    print("-" * 80)
    print(f'{"Área Colaborador":^80}')
    print("-" * 80)
    print("[1] - Cadastrar Voo")
    print("[2] - Alterar Informações de Voo")
    print("[3] - Apagar Voo")
    print("[4] - Voltar ao Menu Anterior")


def exibir_menu_cliente():
    print("-" * 80)
    print(f'{"Área Cliente":^80}')
    print("-" * 80)
    print("[1] - Buscar VOO por Origem: ")
    print("[2] - Buscar VOO por Origem e Destino: ")
    print("[3] - Buscar VOO por Destino: ") 
    print("[4] - Voltar ao Menu Anterior: ")


def cadastrar_voo():
    des_continuar=1
    print("-"*80)           
    print(f'{"Cadastro de VOO":^80}')
    print("-"*80)  

    while des_continuar==1: #castro voo / proximo voo

        l_escala=[]
        #COD_VOO
        while True:
            try:
                cod_voo = int(input("Digite o codigo do voo: "))
                if cod_voo in d_voo.keys():
                    print(f"Codigo ja existente!")
                else:
                    break

            except:
                print("\nERRO: INSIRA SOMENTE NUMEROS!TENTE NOVAMENTE\n")

        #CIDADE DE ORIGEM/DESTINO/NUMERO ESCALAS

        cidade_origem= input("Insira o nome da cidade de origem do voo: ").strip().upper()
        cidade_destino= input("Insira a cidade de destino do voo: ").strip().upper()
        nome_voo=cidade_origem+'/'+cidade_destino
        while True: # escalas
            try:
                n_escalas= int(input("Insira a quantidade de escalas: "))
                for escala in range(1,n_escalas+1):
                    escala = input(f"Insira o nome da {escala}º cidade de escala: ")
                    l_escala.append(escala)                         
                break
            except:
                print("ERRO: INSIRA SOMENTE NUMEROS!")

        while True:  #Conferencia informacoes

            try:
                print( f"\nInformacoes Adicionadas: \n [1] - Codigo Voo: {cod_voo}\n [2] - Cidade de Origem: {cidade_origem}\n [3] - Cidade de Destino: {cidade_destino}") 
                if l_escala!=[]: print(f" [4] - Escalas para {l_escala})\n")
                conf_inf= int(input("As informacoes estao corretas? [1-SIM] OU [2-NAO]: "))
                
                if conf_inf == 1:
                    break
                elif conf_inf>4 or conf_inf<1: #VALIDACAO
                    print("OPCAO INVALIDA: Escolha dentre as opcoes disponiveis!")
                else:
                    print('-'*80)
                    print( f"\n [1] - Codigo Voo: {cod_voo}\n [2] - Cidade de Origem: {cidade_origem}\n [3] - Cidade de Destino: {cidade_destino}\n [4] - Escalas para {l_escala}): ")
                    n_alteracao = int(input("Escolha o item a ser alterado, ou digite [5] para sair: "))
                    if n_alteracao>5 or n_alteracao<1:
                        print("Escolha uma opcao valida!")
                    elif n_alteracao ==5: 
                        break
                    elif n_alteracao ==1:
                        cod_voo = int(input("Digite o codigo do voo: "))
                    elif n_alteracao ==2:
                        cidade_origem= input("Insira o nome da cidade de origem do voo: ").strip().upper()
                        nome_voo=cidade_origem+'/'+cidade_destino

                    elif n_alteracao==3:
                        cidade_destino= input("Insira a cidade de destino do voo: ").strip().upper()
                        nome_voo=cidade_origem+'/'+cidade_destino

                    elif n_alteracao==4:
                        escalas= int(input("Insira a quantidade de escalas: "))
                        for escala in range(1,escalas+1):
                                escala = input(f"Insira o nome da {escala}º cidade de escala: ")
                                l_escala.append(escala)
            except ValueError:
                print("Insira apenas numeros inteiros")

        #Adicionando dicionarios
        d_voo[cod_voo] = [nome_voo,cidade_origem,cidade_destino,n_escalas,l_escala]
        print(d_voo)
        print('-'*80)
        print(f'\n{f"Voo {nome_voo}, adicionado com sucesso!":^80}\n')
        print("-"*80)
        #Continuacao do cadastro
        
        while True:

            try:
                
                continuar=int(input("\nDeseja Inserir Outro VOO?:[1] - SIM   [2] - NAO: "))
                if continuar<1 or continuar>2:
                    print('\nEscolha somente dentre as opçoes desejadas ')
                elif continuar ==1:
                    break
                elif continuar==2:
                    des_continuar=0 ##ERRO DE ATRIBUICAO CORRIGIDO 
                    break
                else:
                    print('')

            except ValueError:

                print("Insira somente numeros!")   



def alterar_voo():
    des_continuar = 1
    print(f"{'Seja Bem Vindo ao Sistema de Alteração de VOO':^150}")

    while des_continuar > 0:
        print("\n\n")
        print("-" * 150)
        print('-' * 150)

        # voos cadastrados
        if len(d_voo) != 0:
            print('-' * 150)
            print(f"| {'Codigo':^10} | {'Nome VOO':^30} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^22} |")
            print('-' * 150)

            for cod_voo, voo_inf in d_voo.items():
                print(f'| {cod_voo:^10} | {str(voo_inf[0]):^30} | {str(voo_inf[1]):^30} | {str(voo_inf[2]):^20} | {str(voo_inf[3]):^20} | {str(voo_inf[4]):^22} |')

                print('-' * 150)

            # alteração
            while True:

                try:
                    des_continuar = int(input("Deseja Alterar Algum VOO?: [1] - SIM    [2] - NÃO: "))


                    if des_continuar == 1:
                        cod_voo_busca = int(input("\nDigite o código do voo que deseja alterar: "))

                        if cod_voo_busca in d_voo.keys():
                            voo_inf = d_voo[cod_voo_busca]

                            cidade_origem = input("Cidade de origem: ")
                            cidade_destino = input("Cidade de destino: ")
                            nome_voo= cidade_origem+'/'+cidade_destino
                            while True:
                                try:
                                    n_escalas = int(input("Insira o número de escalas: "))
                                    break
                                except:
                                    print("Insira apenas números!")

                            l_escala = []

                            for escala in range(1, n_escalas + 1):
                                escala = input(f"Insira o nome da {escala}ª cidade de escala: ")
                                l_escala.append(escala)
                            voo_inf[0] = nome_voo
                            voo_inf[1] = cidade_origem
                            voo_inf[2] = cidade_destino
                            voo_inf[3] = n_escalas
                            voo_inf[4] = l_escala

                            print("\nAlterações realizadas com sucesso!")
                            print("Confira abaixo a tabela de atualizacao dos voos!")
                            break
                        else:
                            print("\nERRO: Este voo não existe!")
                            break
                    elif des_continuar==2:
                        print(f"'\n{'Voltando ao menu principal!':^80}")
                        break
                    else:
                        print(f"{'Digite uma opcao valida!':^80}")

                except ValueError:
                    print("Digite apenas números inteiros!")
                if des_continuar==2:
                    break

            if des_continuar==2:
                break
        else:
            print(f"{'Nenhum voo cadastrado!':^150}")
            break


def apagar_voo():
    print('-' * 150)
    print(f"{'Seja Bem Vindo ao Sistema de Exclusao de VOO':^150}")

    if len(d_voo) == 0:
        print(f'\n{"Nenhum Voo Encontrado! Você Será Redirecionado ao Menu Principal!":^80}')
    else:
        des_continuar = 1
        while des_continuar == 1:
            print('-' * 150)
            print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
            print('-' * 150)

            for cod_voo, voo_inf in d_voo.items():
                print(f'| {cod_voo:^10} | {str(voo_inf[0]):^20} | {str(voo_inf[1]):^30} | {str(voo_inf[2]):^20} | {str(voo_inf[3]):^20} | {str(voo_inf[4]):^32} |')

            print('-' * 150)

            # Exclusao
            while True:
                try:
                    des_continuar = int(input("Deseja Excluir Algum VOO?: [1] - SIM    [2] - NÃO: "))

                    if des_continuar == 1:
                        cod_voo_busca = int(input("\nDigite o código do voo que deseja excluir: "))
                    else:
                        break
                except ValueError:
                    print("Digite apenas números inteiros!")

                if cod_voo_busca in d_voo.keys():
                    d_voo.pop(cod_voo_busca)
                    print("\nVoo EXCLUIDO COM SUCESSO")
                    break


def consultar_voo(): # cidade de origem
    print("-" * 80)
    print(f'{"Consulta de Voo por Origem":^80}')
    print("-" * 80)

    while True:
        nome_origem = input("Digite o nome da cidade de origem: ").strip().upper()
        c = 0
        print(f'\n|{f"VOOS DISPONIVEIS PARA: {nome_origem}":^149}|')
        print('-' * 150)
        print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
        print('-' * 150)

        for codigo, cidade in d_voo.items():
            if cidade[1] == nome_origem:
                print(f'| {codigo:^10} | {str(cidade[0]):^20} | {str(cidade[1]):^30} | {str(cidade[2]):^20} | {str(cidade[3]):^20} | {str(cidade[4]):^32} |')
                print('-' * 150)
                c = 1
        if c == 0:
            print(f"|{f'Sem Voo Disponiveis! Para a cidade {nome_origem}':^150}|")

        buscar_novamente = int(input("Deseja buscar outra cidade? [1] - Sim  [2] - Nao: "))
        if buscar_novamente == 2:
            break
        else:
            print("")


def consultar_voo_cidades(): #cidade origem/destino
    print("-" * 80)
    print(f"{'Busca por Cidade de Origem!':^80}")
    print("-" * 80)

    while True:
        cidade_origem = input("Insira o nome da cidade de ORIGEM: ").strip().upper()
        cidade_destino = input("Insira o nome da cidade de DESTINO: ").strip().upper()
        l_escala = []
        C = 0
        
        for cid, cidade in d_voo.items():
            if cidade[1] == cidade_origem and cidade[2] == cidade_destino:
                l_escala.append(cidade[3])
            
            elif cidade[1] != cidade_origem or cidade[2] != cidade_destino:
                C = 1
        
        if C == 0:
            print("Nenhum voo cadastrado nesta origem!")
        
        if len(l_escala) > 0:
            menor_escala = min(l_escala)
            
            for cid, cidade in d_voo.items():
                if cidade[3] == menor_escala:
                    if cidade[1] == cidade_origem and cidade[2] == cidade_destino:
                        voo = d_voo[cid]
                        
                        print(f'\n{f"|| VOOS DISPONIVEIS COM MENOR ESCALA: {cidade_origem} ||":^150}')
                        print('-' * 150)
                        print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
                        print('-' * 150)
                        print(f'| {cid:^10} | {str(voo[0]):^20} | {str(voo[1]):^30} | {str(voo[2]):^20} | {str(voo[3]):^20} | {str(voo[4]):^32} |')
                        print('-' * 150)
        deseja_continuar=int(input("Deseja realizar outra busca? [1] - SIM   [2] - NAO : "))
        if deseja_continuar==1:
            print("Realize outra busca!")
        else:
            print('')
            break

def consultar_voo_destino(): # cidade de origem
    print("-" * 80)
    print(f'{"Consulta de Voo por Destino":^80}')
    print("-" * 80)

    while True:
        nome_destino = input("Digite o nome da cidade de destino: ").strip().upper()
        c = 0
        print(f'\n|{f"VOOS DISPONIVEIS PARA: {nome_destino}":^149}|')
        print('-' * 150)
        print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
        print('-' * 150)

        for codigo, cidade in d_voo.items():
            if cidade[2] == nome_destino:
                print(f'| {codigo:^10} | {str(cidade[0]):^20} | {str(cidade[1]):^30} | {str(cidade[2]):^20} | {str(cidade[3]):^20} | {str(cidade[4]):^32} |')
                print('-' * 150)
                c = 1
        if c == 0:
            print(f"|{f'Sem Voo Disponiveis! Para a cidade {nome_destino}':^150}|")

        buscar_novamente = int(input("Deseja buscar outra cidade? [1] - Sim  [2] - Nao: "))
        if buscar_novamente == 2:
            break
        else:
            print("")

while True:
    exibir_menu()

    try:
        opc_menu = int(input("Digite a opção escolhida: "))
    except ValueError:
        print("ERRO: Informe apenas números!")
        continue

    if opc_menu == 3:
        print("-" * 80)
        print(f'{"Obrigado! Volte Sempre!":^80}')
        break

    elif opc_menu == 2:
        while True:
            exibir_menu_colaborador()

            try:
                opc_menu_colab = int(input("Digite a opção escolhida: "))
            except ValueError:
                print("ERRO: Informe apenas números!")
                continue

            if opc_menu_colab == 4:
                break

            elif opc_menu_colab == 1:
                cadastrar_voo()

            elif opc_menu_colab == 2:
                alterar_voo()

            elif opc_menu_colab == 3:
                apagar_voo()

            else:
                print("Opção inválida!")

    elif opc_menu == 1:
        while True:
            exibir_menu_cliente()

            try:
                opc_menu_cliente = int(input("Digite a opção escolhida: "))
            except ValueError:
                print("ERRO: Informe apenas números!")
                continue

            if opc_menu_cliente == 4:
                break

            elif opc_menu_cliente == 1: #busca por cidade
                consultar_voo()
            elif opc_menu_cliente == 2: #busca por cid_orig/cid_destino
                consultar_voo_cidades()
            elif opc_menu_cliente == 3:
                consultar_voo_destino()
            else:
                print("Opção inválida!")

    else:
        print("Opção inválida!")
