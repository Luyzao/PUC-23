
import oracledb
try:

    conexao = oracledb.connect(
        user="bd2402231135",
        password="Lfwhj7",
        dsn="172.16.12.14/XE"
)
       
except Exception as err:
        print('ERRO',err)
else:
    

        # MENU

        
        while True:
            print(f"1.CLASSIFICAR\n2.INSERIR\n3.EDITAR\n4.EXCLUIR\n5.SAIR")
            opc = int(input("DIGITE UMA DAS OPÇÕES: "))
            
            # QUALIFICAR
            
            if opc == 1:
                
                cursor = conexao.cursor()
                quant = 0
                mp10 = 0
                mp2_5 = 0
                o3 = 0
                co = 0
                no2 = 0
                so2 = 0
                for i in cursor.execute("select * from indice"):
                    print("deixa cria algo bonito aqui Lais")

                for num in cursor.execute("select codigo from indice"):
                    quant += 1

                for num in cursor.execute("select mp10 from indice"):
                    mp10 += sum(num)
                mmp10 = mp10/quant

                for num in cursor.execute("select mp2_5 from indice"):
                    mp2_5 += sum(num)
                mmp2_5 = mp2_5 / quant

                for num in cursor.execute("select o3 from indice"):
                    o3 += sum(num)
                mo3 = o3 / quant

                for num in cursor.execute("select co from indice"):
                    co += sum(num)
                mco = co / quant

                for num in cursor.execute("select no2 from indice"):
                    no2 += sum(num)
                mno2 = no2 / quant

                for num in cursor.execute("select so2 from indice"):
                    so2 += sum(num)
                mso2 = so2 / quant

                # EFEITOS

                if mmp10 < 0 or mmp2_5 < 0 or mo3 < 0 or mco < 0 or mno2 < 0 or mso2 < 0:
                    print("Algum índice esta com o valor inválido! \n Reescreva os dados, por favor.")
                    continue
                else:
                    if mmp10 > 250 or mmp2_5 > 125 or mo3 > 200 or mco > 15 or mno2 > 1130 or mso2 > 800:
                        print(
                            "A qualidade do ar está PÉSSIMA!\n\nEfeitos na saíde: Toda a população pode apresentar sérios riscos de \nmanifestação de doenças respiratórias e \ncardiovasculares. Aumento de mortes prematuras \nem pessoas de grupos sensíveis.")
                    elif 150 < mmp10 <= 250 or 75 < mmp2_5 <= 125 or 160 < mo3 <= 200 or 13 < mco <= 15 or 320 < mno2 <= 1130 or 365 < mso2 <= 800:
                        print(
                            "A qualidade do ar está MUITO RUIM!\n\nEfeitos na saúde: Toda a população pode apresentar agravamento dos \nsintomas como tosse seca, cansaço, ardor nos olhos, \nnariz e garganta, além de falta de ar e respiração \nofegante. Efeitos ainda mais graves à saúde de \ngrupos sensíveis (crianças, idosos e pessoas com \ndoenças respiratórias e cardíacas).")
                    elif 100 < mmp10 <= 150 or 50 < mmp2_5 <= 75 or 130 < mo3 <= 160 or 11 < mco <= 13 or 240 < mno2 <= 320 or 40 < mso2 <= 365:
                        print(
                            "A qualidade do ar está RUIM!\n\nEfeitos na saúde: Toda a população pode apresentar sintomas como \ntosse seca, cansaço, ardor nos olhos, nariz e \ngarganta. Pessoas de grupos sensíveis (crianças, idosos e \npessoas com doenças respiratórias e \ncardíacas) podem apresentar efeitos mais sérios na saúde.")
                    elif 50 < mmp10 <= 100 or 25 < mmp2_5 <= 50 or 100 < mo3 <= 130 or 9 < mco <= 11 or 200 < mno2 <= 240 or 20 < mso2 <= 40:
                        print(
                            "A qualidade do ar está REGULAR!\n\nEfeitos na saúde: Pessoas de grupos sensiveis (crianças, idosos e \npessoas com doenças respiratórias e cardíacas) \npodem apresentar sintomas como tosse seca e \ncansaço. A população, em geral, não é afetada.")
                    elif mmp10 <= 50 or mmp2_5 <= 25 or mo3 <= 100 or mco <= 9 or mno2 <= 200 or mso2 <= 20:
                        print("A qualidade do ar está BOA!\n\nEfeitos na saúde: Nenhum efeito na saúde.")
                  
                OPC = int(input("VOCÊ QUER VOLTAR PARA O MENU?\n1.SIM\n2.NÃO QUERO SAIR DO PROGRAMA\n"))
                            
                if(OPC == 1):

                    continue
                                
                elif OPC == 2:
                     exit
                else:
                        print("ESSA OPÇÂO NÃO EXISTE") 
                
                break
            
                
                
            # INSERIR 
            
            
            
            elif opc ==2:
                
                cursor = conexao.cursor()

                mp10 = int(input("MP10: "))
                mp2_5 = int(input("MP2,5: "))
                fmc = int(input("FMC: "))
                o3 = int(input("O3: "))
                co = int(input("CO: "))
                no2 = int(input("NO2: "))
                so2 = int(input("SO2: "))
                    
                cursor.execute(f'INSERT INTO indice (MP10,MP2_5,FMC,O3,CO,NO2,SO2) VALUES ({mp10},{mp2_5},{fmc},{o3},{co},{no2},{so2})')
                
                salvar = int(input("VOCÊ DESEJA SALVAR VOLTAR PARA MENU?\n1.SIM\n2.NÃO APENAS IR PARA O MENU\n"))
                if salvar == 1:
                    conexao.commit() 
                    continue
                   
                elif salvar == 2:
                    print("VOLTANDO PARA O MENU")
                    continue
                else:
                    print("ESTÁ OPÇÃO NÃO EXISTE. ")
                
                break
            
            
            # ALTERAR
            
            
            elif opc ==3:
                
                cursor = conexao.cursor()
                
                sql = (f"SELECT codigo FROM indice")
                for i in cursor.execute(sql):
                                print (f"OPÇÃO: {i}")
                                
                id = int(input("QUAL OPÇÃO VOCÊ QUER ALTERA?\nOPÇÃO: "))
                
                opcao = (f"SELECT MP10,MP2_5,FMC,O3,CO,NO2,SO2 FROM indice WHERE codigo = {id}")
                for i in cursor.execute(opcao):
                                print (f"OPÇÃO ESCOLHIDDA: {i}")
                
            
                mp10 = int(input("MP10: "))
                mp2_5 = int(input("MP2,5: "))
                fmc = int(input("FMC: "))
                o3 = int(input("O3: "))
                co = int(input("CO: "))
                no2 = int(input("NO2: "))
                so2 = int(input("SO2: "))
                
                alterar =(f"UPDATE indice SET MP10 = {mp10},MP2_5 = {mp2_5}, FMC = {fmc}, O3 = {o3}, CO = {co},NO2 = {no2},SO2 = {so2} WHERE codigo = {id}")
                cursor.execute(alterar)
                
                
                
                conf = int(input("VOCÊ REALEMENTE QUER ALTERAR?\n1.SIM\n2.NÃO, VOLTAR PARA O MENU\nOPÇÃO: "))
                
                if conf == 1:
                    
                        conexao.commit()
                        
                        continue
                elif conf == 2:
                    continue
                else:
                    print("ESTA OPÇÃO NÃO EXISTE.")
                
                break
            
            
            # DELETAR
            
            
            elif opc ==4:
                
                cursor = conexao.cursor()
                
                sql = (f"SELECT codigo FROM indice")
                for i in cursor.execute(sql):
                                print (f"OPÇÃO: {i}")
                id = int(input("QUAL OPÇÃO VOCÊ DESEJA DELETAR?\nOPÇÃO: "))
                
                delete = (f"DELETE FROM indice WHERE codigo = {id} ")
                cursor.execute(delete)
                print(cursor.rowcount,"record(s) deleted")
                
                
                conf = int(input("VOCÊ REALEMENTE QUER DELETAR?\n1.SIM\n2.NÃO, VOLTAR PARA O MENU\nOPÇÃO: "))
                
                if conf == 1:
                    
                        conexao.commit()
                        
                        continue
                elif conf == 2:
                    continue
                else:
                    print("ESTA OPÇÃO NÃO EXISTE.")
                    
                break
            elif opc ==5:
                conexao.close()
                break
            else:
                print("DIGITE UMA OPÇÂO VÁLIDA.")
     
