##Segunda Fase

import os

##Conexao Banco de Dados
import oracledb
try:
    conexao = oracledb.connect( user="bd2402231116", password="Ktcfq3", dsn="172.16.12.14/XE")
except:
    print("Erro durante a conexao!")


##Criar tabela

else: 

    #Verificar se a tabela existe
    try:
            
        tlbVer = conexao.cursor()  # cria a variavel conexao cursos
        tlbVer.execute("SELECT * FROM indice")
    #Cria a tabela caso nao exista
    except:
        
        tlbVer.execute("CREATE TABLE indice(codigo NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, nome VARCHAR(100),mp10 float,mp2_5 float,o3 float,co float,no2 float,so2 float)")

    def imprimir_tabela():
        print(f"{'='*105}")
        print(f"| {'CODIGO':^10} | {'NOME':^10} | {'MP10':^10} | {'MP2,5':^10} | {'O3':^10} | {'CO':^10} | {'NO2':^10} | {'SO2':^10} |")
        print(f"{'='*105}")

        for i in range(1):

            codL =[]
            cod = (f"SELECT codigo FROM indice")
            for i in cursor.execute(cod):
                cod = int(''.join(map(str, i)))
                codL.append(cod) 

            nomeL =[]
            nome = (f"SELECT nome FROM indice")
            for i in cursor.execute(nome):
                nome = ''
                nome += str(''.join(map(str, i)))
                for j in i:
                    nomeL.append(nome) 

            mp10L =[]
            mp10 = (f"SELECT mp10 FROM indice")
            for i in cursor.execute(mp10):
                mp10 = float(''.join(map(str, i)))
                mp10L.append(mp10) 

            mp2L =[]
            mp2 = (f"SELECT mp2_5 FROM indice")
            for i in cursor.execute(mp2):
                mp2 = float(''.join(map(str, i)))
                mp2L.append(mp2) 

            o3L =[]
            o3 = (f"SELECT o3 FROM indice")
            for i in cursor.execute(o3):
                o3 = float(''.join(map(str, i)))
                o3L.append(o3) 

            coL =[]
            co = (f"SELECT co FROM indice")
            for i in cursor.execute(co):
                co = float(''.join(map(str, i)))
                coL.append(co) 

            no2L =[]
            no2 = (f"SELECT no2 FROM indice")
            for i in cursor.execute(no2):
                no2 = float(''.join(map(str, i)))
                no2L.append(no2) 

            so2L =[]
            so2 = (f"SELECT so2 FROM indice")
            for i in cursor.execute(so2):
                so2 = float(''.join(map(str, i)))
                so2L.append(so2) 

            imprimirTudo =("SELECT COUNT(*) FROM indice")
            for i in cursor.execute(imprimirTudo):
                imprimirTudo = int(''.join(map(str, i)))

            for i in range(imprimirTudo):
            
                print(f"| {codL[i]:^10} | {nomeL[i]:^10} | {mp10L[i]:^10} | {mp2L[i]:^10} | {o3L[i]:^10} | {coL[i]:^10} | {no2L[i]:^10} | {so2L[i]:^10} |")
                print(f"{'-'*105}")
            print(f"\t{'='*69}")


    #Sistema de classificacao do ar
            
    print(f"\t| {'BEM - VINDO AO QUALIFICADOR DE AR':^65} |")
    print(f"\t{'='*69}")
    
##Entradas Dados

print(f'\n{"Classificacao da Qualidade do AR":^40}')

while True:
    print("\nInsira os parametros solicitados abaixo: \n")
    try:
        MP10= float(input("Insira o valor de particulas inalaveis (MP10): "))
        MP25 = float(input("Insira o valor de particulas finas (MP2.5): "))
        O3 = float(input("Insira o valor do ozonio (O3): "))
        CO = float(input("Insira o valor do monoxido de carbono (CO): "))
        NO2 = float(input("Insira o valor do dioxido de nitrogenio (NO2): "))
        SO2 = float(input("Insira o valor do dioxido de enxofre (SO2): "))
    except:
        print(f"\n{'ERRO!':^40}")
        print(f"{'Insira apenas numeros!':^40}")
        
    if MP10<0 or MP25<0 or O3<0 or CO<0 or NO2<0 or SO2<0:
        print("\nInsira apenas valores positivos!") 
    else:
        break

##Classificacao do ar

print(f'\n{"Resultado":^40}')

if MP10<50 and MP25<25 and O3<100 and CO<9 and NO2<200 and SO2<20:
    print(('-')*40)
    print(f"\n{'A qualidade do ar esta BOA!':^40}")
    print(f"{'Nao a maleficios a saude!':^40}")
    print(('-')*40)
elif MP10<100 and MP25<50 and O3<130 and CO<11 and NO2<240 and SO2<40:
    print(('-')*40)
    print(f"\n{'A qualidade do ar esta MODERADA!':^40}")
    print(f"{'Pessoas de grupos sensiveis podem apresentar sintomas como tosse seca e cansaco. A populacao, em geral nao e afetada'}")
    print(('-')*40)

elif MP10<150 and MP25<75 and O3<160 and CO<13 and NO2<320 and SO2<365:
    print(('-')*40)
    print(f"\n{'A qualidade do ar esta RUIM!':^40}")
    print(f"{'Toda a populacao pode apresentar sintomas como tosse seca, cansaco, ardor nos olhos, nariz e garganta.'}")
    print(f"{'Pessoas de grupos sensiveis, podem apresentar efeitos mais serios na saude'}")
    print(('-')*40)

elif MP10<250 and MP25<125 and O3<200 and CO<15 and NO2<1130 and SO2<800:
    print(('-')*40)
    print(f"\n{'A qualidade do ar esta MUITO RUIM!':^40}")
    print(f"{'Toda a poplacao pode apresentar agravamento dos sintomas como tosse seca, cansaco,ardor nos olhos,nariz e garganta'}")
    print(f"{'e ainda falta de ar e respiracao ofegante. Efeitos ainda mais graves a saude de grupos sensiveis'}")
    print(('-')*40)

elif MP10<250 and MP25<125 and O3<200 and CO<15 and NO2<1130 and SO2<800:
    print(('-')*40)
    print(f"\n{'A qualidade do ar esta PESSIMA!':^40}")
    print(f"{'Toda a poplacao pode apresentar agravamento dos sintomas como tosse seca, cansaco,ardor nos olhos,nariz e garganta'}")
    print(f"{'e ainda falta de ar e respiracao ofegante. Efeitos ainda mais graves a saude de grupos sensiveis'}")
    print(('-')*40)                 