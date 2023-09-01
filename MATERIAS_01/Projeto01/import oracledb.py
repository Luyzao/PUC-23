import oracledb
import os
try:
    conexao = oracledb.connect(
        user="bd2402231135",
        password="Lfwhj7",
        dsn="172.16.12.14/XE"
)
       
except Exception as err:
        print('ERRO',err)
else:
    

        # CRIANDO TABELA CASO NÂO EXISTA

        try:
             
            tlbVer = conexao.cursor()
            tlbVer.execute("SELECT * FROM indice")
        
        except:
            
            tlbVer.execute("CREATE TABLE indice(codigo NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, nome VARCHAR(100),mp10 float,mp2_5 float,o3 float,co float,no2 float,so2 float)")

        def imprmirTabela():
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

        os.system('cls')
        
        print(f"\t{'='*69}")
        print(f"\t| {'BEM - VINDO AO QUALIFICADOR DE AR':^65} |")
        print(f"\t{'='*69}")

        # MENU
        
        while True:
           
            print(f"\n\t {'MENU':^65} ")
            print(f"\t{'='*69}")
            print(f"\t| {'1.INSERIR':^10} | {'2.ALTERAR':^10} | {'3.EXCLUIR':^10} | {'4.CLASSIFICAR':^10} | {'5.SAIR':^10} |")
            print(f"\t{'='*69}")

            while True:
                try:
                    opc = int(input("\tDIGITE UMA DAS OPÇÕES: "))
                    break
                except:
                    print("\tApenas numeros\n")

            # QUALIFICAR
            
            if opc == 4:
                
                cursor = conexao.cursor()

                vrf = cursor.execute("SELECT COUNT(codigo) FROM indice")
                for i in vrf:
                      vrf = int(''.join(map(str, i)))

                if vrf == 0:
                    os.system('cls')
                    print(f"\n\t{'-'*69}")
                    print(f"\t| {'Nenhuma amostra inserida!':^65} |")
                    print(f"\t{'-'*69}")
                    print(f"\t{'-'*69}")
                    print(f"\t| {'Insira uma amostrar para classificar':^65} |")
                    print(f"\t{'-'*69}\n")
                    
                else:
    
                    while True:

                        Vmp10 = (f"SELECT SUM(mp10)/COUNT(mp10) FROM indice")
                        for i in cursor.execute(Vmp10):
                            mp10 = float(''.join(map(str, i)))

                        Vmp2_5 = (f"SELECT SUM(mp2_5)/COUNT(mp2_5) FROM indice")
                        for i in cursor.execute(Vmp2_5):
                            mp2_5 = float(''.join(map(str, i)))

                        Vo3 = (f"SELECT SUM(O3)/COUNT(o3) FROM indice")
                        for i in cursor.execute(Vo3):
                            o3 = float(''.join(map(str, i)))

                        Vco = (f"SELECT SUM(co)/COUNT(co) FROM indice")
                        for i in cursor.execute(Vco):
                            co = float(''.join(map(str, i)))

                        Vno2 = (f"SELECT SUM(no2)/COUNT(no2) FROM indice")
                        for i in cursor.execute(Vno2):
                            no2 = float(''.join(map(str, i)))

                        Vso2 = (f"SELECT SUM(so2)/COUNT(so2) FROM indice")
                        for i in cursor.execute(Vso2):
                            so2 = float(''.join(map(str, i)))



                            #EFEITOS

                        if mp10 < 0 or mp2_5 < 0 or o3 < 0 or co < 0 or no2 < 0 or so2 < 0:
                            print("Algum índice esta com o valor inválido! \n Reescreva os dados, por favor.")
                            break
                        else:
                            if mp10 > 250 or mp2_5 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 >800:
                                os.system('cls')
                                print(f"\n\t{'='*69}")
                                print(f"\t| {'A qualidade do ar está PÉSSIMA!':^65} |")
                                print(f"\t{'-'*69}")
                                print(f"\t| {'Efeitos na saíde:':^65} |\n\t{'-'*69}\n\t| {'Toda a população pode apresentar sérios riscos de':^65} |\n\t| {'manifestação de doenças respiratórias e':^65} |\n\t| {'cardiovasculares. Aumento de mortes prematuras':^65} |\n\t| {'em pessoas de grupos sensíveis.':^65} |")
                                print(f"\t{'='*69}\n\n")

                            elif 150 < mp10 <= 250 or 75 < mp2_5 <= 125 or 160 < o3 <= 200 or 13 < co <= 15 or 320 < no2 <= 1130 or 365 < so2 <= 800:
                                os.system('cls')
                                print(f"\n\t{'='*69}")
                                print(f"\t| {'A qualidade do ar está MUITO RUIM!':^65} |")
                                print(f"\t{'-'*69}")
                                print (f"\t| {'Efeitos na saúde:':^65} |\n\t{'-'*69}\n\t| {'Toda a população pode apresentar agravamento dos':^65} |\n\t| {'sintomas como tosse seca, cansaço, ardor nos olhos,':^65} |\n\t| {'nariz e garganta, além de falta de ar e respiração':^65} |\n\t| {'ofegante. Efeitos ainda mais graves à saúde de':^65} |\n\t| {'grupos sensíveis (crianças, idosos e pessoas com':^65} |\n\t| {'doenças respiratórias e cardíacas).':^65} |")
                                print(f"\t{'='*69}\n\n")

                            elif 100 < mp10 <= 150 or 50 < mp2_5 <= 75 or 130 < o3 <= 160 or 11 < co <= 13 or 240 < no2 <= 320 or 40 < so2 <= 365:
                                os.system('cls')
                                print(f"\n\t{'='*69}")
                                print(f"\t| {'A qualidade do ar está RUIM!':^65} |")
                                print(f"\t{'-'*69}")
                                print (f"\t| {'Efeitos na saúde:':^65} |\n\t{'-'*69}\n\t| {'Toda a população pode apresentar sintomas como':^65} |\n\t| {'tosse seca, cansaço, ardor nos olhos, nariz e':^65} |\n\t| {'garganta. Pessoas de grupos sensíveis (crianças, idosos e':^65} |\n\t| {'pessoas com doenças respiratórias e':^65} |\n\t| {'cardíacas) podem apresentar efeitos mais sérios na saúde.':^65} |")
                                print(f"\t{'='*69}\n\n")
                                
                            elif 50 < mp10 <= 100 or 25 < mp2_5 <= 50 or 100 < o3 <= 130 or 9 < co <= 11 or 200 < no2 <= 240 or 20 < so2 <= 40:
                                os.system('cls')
                                print(f"\n\t{'='*69}")
                                print(f"\t| {'A qualidade do ar está REGULAR!':^65} |")
                                print(f"\t{'-'*69}")
                                print (f"\t| {'Efeitos na saúde:':^65} |\n\t{'-'*69}\n\t| {'Pessoas de grupos sensiveis (crianças, idosos e':^65} |\n\t| {'pessoas com doenças respiratórias e cardíacas)':^65} |\n\t| {'podem apresentar sintomas como tosse seca e':^65} |\n\t| {'cansaço. A população, em geral, não é afetada.':^65} |")
                                print(f"\t{'='*69}\n\n")

                            elif mp10 <= 50 or mp2_5 <= 25 or o3 <= 100 or co <= 9 or no2 <= 200 or so2 <= 20:
                                os.system('cls')
                                print(f"\n\t{'='*69}")
                                print(f"\t| {'A qualidade do ar está BOA!':^65} |")
                                print(f"\t{'-'*69}")
                                print (f"\n\t| {'Efeitos na saúde:':^65} |\n\t{'-'*69}\n\t| {' Nenhum efeito na saúde.':^65} |\n ")
                                print(f"\t{'='*69}\n\n")

                        print(f"\t{'MEDIA':^65}")
                        print(f"\t{'='*69}")
                        print(f"\t| {'MP10':^9} | {'MP2,5':^8} | {'O3':^8} | {'CO':^8} | {'NO2':^8} | {'SO2':^9} |")
                        print(f"\t{'-'*69}")
                        print(f"\t| {mp10:^9} | {mp2_5:^8} | {o3:^8} | {co:^8} | {no2:^8} | {so2:^9} |")
                        print(f"\t{'='*69}\n\n")

                        break
            
        
            # INSERIR 
              
            elif opc ==1:
                
                cursor = conexao.cursor()
                os.system('cls')
                print(f"\t{'='*69}")
                print(f"\t| {'CADASTRANDO UMA NOVA AMOSTRA':^65} |")
                print(f"\t{'='*69}")

                nome = input(f"\t|- Nome da amostra: ")
                print(f"\t{'_'*69}")
                while True:
                    try:
                        while True:

                            mp10 = int(input(f"\n\t|- MP10: "))
                            print(f"\t{'_'*69}")
                            if mp10 >= 0:
                                 break
                            else:
                                print(f"\n\t{'-'*69}")
                                print(f"\tApenas números positivos")
                                print(f"\t{'-'*69}")
                        break
                    except:
                        print(f"\n\t{'-'*69}")
                        print(f"\tApenas números")
                        print(f"\t{'-'*69}")
                while True:
                    try:
                        while True:

                            mp2_5 = int(input(f"\n\t|- MP2,5: "))
                            print(f"\t{'_'*69}")
                            if mp2_5 >= 0:
                                 break
                            else:
                                print(f"\n\t{'-'*69}")
                                print(f"\tApenas números positivos")
                                print(f"\t{'-'*69}")
                        break
                    except:
                        print(f"\n\t{'-'*69}")
                        print(f"\tApenas números")
                        print(f"\t{'-'*69}")
                while True:
                    try:
                        while True:

                            o3 = int(input(f"\n\t|- O3: "))
                            print(f"\t{'_'*69}")
                            if o3 >= 0:
                                 break
                            else:
                                print(f"\n\t{'-'*69}")
                                print(f"\tApenas números positivos")
                                print(f"\t{'-'*69}")
                        break
                    except:
                        print(f"\n\t{'-'*69}")
                        print(f"\tApenas números")
                        print(f"\t{'-'*69}")
                while True:
                    try:
                        while True:

                            co = int(input(f"\n\t|- CO: "))
                            print(f"\t{'_'*69}")
                            if co >= 0:
                                 break
                            else:
                                print(f"\n\t{'-'*69}")
                                print(f"\tApenas números positivos")
                                print(f"\t{'-'*69}")
                        break
                    except:
                        print(f"\n\t{'-'*69}")
                        print(f"\tApenas números")
                        print(f"\t{'-'*69}")
                while True:
                    try:
                        while True:

                            no2 = int(input(f"\n\t|- NO2: "))
                            print(f"\t{'_'*69}")
                            if no2 >= 0:
                                 break
                            else:
                                print(f"\n\t{'-'*69}")
                                print(f"\tApenas números positivos")
                                print(f"\t{'-'*69}")
                        break        
                    except:
                        print(f"\n\t{'-'*69}")
                        print(f"\tApenas números")
                        print(f"\t{'-'*69}")
                while True:
                    try:
                        while True:

                            so2 = int(input(f"\n\t|- SO2: "))
                            print(f"\t{'_'*69}")
                            if so2 >= 0:
                                 break
                            else:
                                print(f"\n\t{'-'*69}")
                                print(f"\tApenas números positivos")
                                print(f"\t{'-'*69}")
                        break
                    except:
                         print(f"\n\t{'-'*69}")
                         print(f"\tApenas números")
                         print(f"\t{'-'*69}")
                    
                cursor.execute(f"INSERT INTO indice (NOME,MP10,MP2_5,O3,CO,NO2,SO2) VALUES ('{nome}',{mp10},{mp2_5},{o3},{co},{no2},{so2})")
                conexao.commit() 
                os.system('cls')
               
            
            
            # ALTERAR
            
            
            elif opc ==2:

                os.system('cls')
                print(f"\t{'='*69}")
                print(f"\t| {'ALTERAR UMA AMOSTRA':^65} |")
                print(f"\t{'='*69}")
                
                cursor = conexao.cursor()

                vrf = cursor.execute("SELECT COUNT(codigo) FROM indice")
                for i in vrf:
                      vrf = int(''.join(map(str, i)))

                if vrf == 0:
                    print("Não nenhuma amostra!")
                    
                else:
                    controle = 0
                    while controle == 0:

                        imprmirTabela()

                        dltList = []
                        sql = (f"SELECT codigo FROM indice")
                        for i in cursor.execute(sql):
                            dlt = int(''.join(map(str, i)))
                            dltList.append(dlt)          
                        id = int(input("DIGITE O CODIGO DA AMOSTRA: "))

                        for i in range(len(dltList)):    
                            if id not in dltList:
                                
                                print("Esta opção não existe")
                                break
                            else:

                                while True:
                                    try:
                                        while True:

                                            mp10 = int(input(f"\n\t|- MP10: "))
                                            print(f"\t{'_'*69}")
                                            if mp10 >= 0:
                                                break
                                            else:
                                                print(f"\n\t{'-'*69}")
                                                print(f"\tApenas números positivos")
                                                print(f"\t{'-'*69}")
                                        break
                                    except:
                                        print(f"\n\t{'-'*69}")
                                        print(f"\tApenas números")
                                        print(f"\t{'-'*69}")
                                while True:
                                    try:
                                        while True:

                                            mp2_5 = int(input(f"\n\t|- MP2,5: "))
                                            print(f"\t{'_'*69}")
                                            if mp2_5 >= 0:
                                                break
                                            else:
                                                print(f"\n\t{'-'*69}")
                                                print(f"\tApenas números positivos")
                                                print(f"\t{'-'*69}")
                                        break
                                    except:
                                        print(f"\n\t{'-'*69}")
                                        print(f"\tApenas números")
                                        print(f"\t{'-'*69}")
                                while True:
                                    try:
                                        while True:

                                            o3 = int(input(f"\n\t|- O3: "))
                                            print(f"\t{'_'*69}")
                                            if o3 >= 0:
                                                break
                                            else:
                                                print(f"\n\t{'-'*69}")
                                                print(f"\tApenas números positivos")
                                                print(f"\t{'-'*69}")
                                        break
                                    except:
                                        print(f"\n\t{'-'*69}")
                                        print(f"\tApenas números")
                                        print(f"\t{'-'*69}")
                                while True:
                                    try:
                                        while True:

                                            co = int(input(f"\n\t|- CO: "))
                                            print(f"\t{'_'*69}")
                                            if co >= 0:
                                                break
                                            else:
                                                print(f"\n\t{'-'*69}")
                                                print(f"\tApenas números positivos")
                                                print(f"\t{'-'*69}")
                                        break
                                    except:
                                        print(f"\n\t{'-'*69}")
                                        print(f"\tApenas números")
                                        print(f"\t{'-'*69}")
                                while True:
                                    try:
                                        while True:

                                            no2 = int(input(f"\n\t|- NO2: "))
                                            print(f"\t{'_'*69}")
                                            if no2 >= 0:
                                                break
                                            else:
                                                print(f"\n\t{'-'*69}")
                                                print(f"\tApenas números positivos")
                                                print(f"\t{'-'*69}")
                                        break        
                                    except:
                                        print(f"\n\t{'-'*69}")
                                        print(f"\tApenas números")
                                        print(f"\t{'-'*69}")
                                while True:
                                    try:
                                        while True:

                                            so2 = int(input(f"\n\t|- SO2: "))
                                            print(f"\t{'_'*69}")
                                            if so2 >= 0:
                                                break
                                            else:
                                                print(f"\n\t{'-'*69}")
                                                print(f"\tApenas números positivos")
                                                print(f"\t{'-'*69}")
                                        break
                                    except:
                                        print(f"\n\t{'-'*69}")
                                        print(f"\tApenas números")
                                        print(f"\t{'-'*69}")
                                
                            
                                update = (f"UPDATE indice SET MP10 = {mp10},MP2_5 = {mp2_5}, O3 = {o3}, CO = {co},NO2 = {no2},SO2 = {so2} WHERE codigo = {id}")
                                cursor.execute(update)
                                conexao.commit()
                                controle = 1
                                os.system('cls')
                                break

                       
            
            # DELETAR
                
            elif opc ==3:

                os.system('cls')
                print(f"\t{'='*69}")
                print(f"\t| {'DELETANDO UMA AMOSTRA':^65} |")
                print(f"\t{'='*69}")

                cursor = conexao.cursor()
                vrf = cursor.execute("SELECT COUNT(codigo) FROM indice")
                for i in vrf:
                      vrf = int(''.join(map(str, i)))

                if vrf == 0:
                    print("Não nenhuma amostra!")
                    
                else:

                    controle = 0
                    while controle == 0:

                        imprmirTabela()
                            
                        dltList = []
                        sql = (f"SELECT codigo FROM indice")
                        for i in cursor.execute(sql):
                            dlt = int(''.join(map(str, i)))
                            dltList.append(dlt)  
     
                        id = int(input("DIGITE O CODIGO DA AMOSTRA: "))
                        
                        for i in range(len(dltList)):    
                            if id not in dltList:
                                
                                print("Esta opção não existe")
                                break
                                
                            else:
                            
                                delete = (f"DELETE FROM indice WHERE codigo = {id} ")
     
                                cursor.execute(delete)
                                conexao.commit()
                                print(cursor.rowcount,"record(s) deleted")       
                                controle = 1
                                os.system('cls')
                                break
                                       
       
                        
            elif opc ==5:
                conexao.close()
                os.system('cls')
                break
            else:
                print("DIGITE UMA OPÇÂO VÁLIDA.")
            

       
            
        
    
    
    
    
    

    


        
    



    