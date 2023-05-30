import getpass
import oracledb
try:
    conexao = oracledb.connect(
        user = "Valentina",
        password = "valeenzo",
        dsn="localhost/XEPDB1"
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
                
                sql = (f"SELECT id_indice FROM indice")
                for i in cursor.execute(sql):
                                print (f"OPÇÃO: {i}")
                    
                id=input("DIGITE QUAL OPÇÃO VOCE QUER QUALIFICAR?\n OPÇÃO: ")


                soma = (f"SELECT(MP10 + MP2_5 + O3 + CO + NO2 + SO2) FROM indice WHERE id_indice = {id}")
                for i in cursor.execute(soma):
                    res = int(''.join(map(str, i)))
                    print (res)

                conta = ("SELECT COUNT(*) FROM information_schema.columns WHERE indice")
                for i in cursor.execute(conta):
                    quant = int(''.join(map(str, i)))

                media = res/quant

                Vmp10 = (f"SELECT(MP10) FROM indice WHERE id_indice = {id}")
                for i in cursor.execute(Vmp10):
                    mp10 = int(''.join(map(str, i)))
                
                Vmp2_5 = (f"SELECT(MP2_5) FROM indice WHERE id_indice = {id}")
                for i in cursor.execute(Vmp10):
                    mp2_5 = int(''.join(map(str, i)))
                
                Vo3 = (f"SELECT(O3) FROM indice WHERE id_indice = {id}")
                for i in cursor.execute(Vmp10):
                    o3 = int(''.join(map(str, i)))

                Vco = (f"SELECT(CO) FROM indice WHERE id_indice = {id}")
                for i in cursor.execute(Vmp10):
                    co = int(''.join(map(str, i)))

                Vno2 = (f"SELECT(NO2) FROM indice WHERE id_indice = {id}")
                for i in cursor.execute(Vmp10):
                    no2 = int(''.join(map(str, i)))

                Vso2 = (f"SELECT(SO2) FROM indice WHERE id_indice = {id}")
                for i in cursor.execute(Vmp10):
                    so2 = int(''.join(map(str, i)))
                    
                
                                
                    #EFEITOS
                    
                if mp10 < 0 or mp2_5 < 0 or o3 < 0 or co < 0 or no2 < 0 or so2 < 0:
                    print("Algum índice esta com o valor inválido! \n Reescreva os dados, por favor.")
                    continue
                else:
                    if mp10 > 250 or mp2_5 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 >800:
                        print \
                            ("A qualidade do ar está PÉSSIMA!\n\nEfeitos na saíde: Toda a população pode apresentar sérios riscos de \nmanifestação de doenças respiratórias e \ncardiovasculares. Aumento de mortes prematuras \nem pessoas de grupos sensíveis.")
                    elif 150 < mp10 <= 250 or 75 < mp2_5 <= 125 or 160 < o3 <= 200 or 13 < co <= 15 or 320 < no2 <= 1130 or 365 < so2 <= 800:
                        print \
                            ("A qualidade do ar está MUITO RUIM!\n\nEfeitos na saúde: Toda a população pode apresentar agravamento dos \nsintomas como tosse seca, cansaço, ardor nos olhos, \nnariz e garganta, além de falta de ar e respiração \nofegante. Efeitos ainda mais graves à saúde de \ngrupos sensíveis (crianças, idosos e pessoas com \ndoenças respiratórias e cardíacas).")
                    elif 100 < mp10 <= 150 or 50 < mp2_5 <= 75 or 130 < o3 <= 160 or 11 < co <= 13 or 240 < no2 <= 320 or 40 < so2 <= 365:
                        print \
                            ("A qualidade do ar está RUIM!\n\nEfeitos na saúde: Toda a população pode apresentar sintomas como \ntosse seca, cansaço, ardor nos olhos, nariz e \ngarganta. Pessoas de grupos sensíveis (crianças, idosos e \npessoas com doenças respiratórias e \ncardíacas) podem apresentar efeitos mais sérios na saúde.")
                    elif 50 < mp10 <= 100 or 25 < mp2_5 <= 50 or 100 < o3 <= 130 or 9 < co <= 11 or 200 < no2 <= 240 or 20 < so2 <= 40:
                        print \
                            ("A qualidade do ar está REGULAR!\n\nEfeitos na saúde: Pessoas de grupos sensiveis (crianças, idosos e \npessoas com doenças respiratórias e cardíacas) \npodem apresentar sintomas como tosse seca e \ncansaço. A população, em geral, não é afetada.")
                    elif mp10 <= 50 or mp2_5 <= 25 or o3 <= 100 or co <= 9 or no2 <= 200 or so2 <= 20:
                        print \
                            ("A qualidade do ar está BOA!\n\nEfeitos na saúde: Nenhum efeito na saúde.")
                   
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
                
                sql = (f"SELECT id_indice FROM indice")
                for i in cursor.execute(sql):
                                print (f"OPÇÃO: {i}")
                                
                id = int(input("QUAL OPÇÃO VOCÊ QUER ALTERA?\nOPÇÃO: "))
                
                opcao = (f"SELECT MP10,MP2_5,FMC,O3,CO,NO2,SO2 FROM indice WHERE id_indice = {id}")
                for i in cursor.execute(opcao):
                                print (f"OPÇÃO ESCOLHIDDA: {i}")
                
            
                mp10 = int(input("MP10: "))
                mp2_5 = int(input("MP2,5: "))
                fmc = int(input("FMC: "))
                o3 = int(input("O3: "))
                co = int(input("CO: "))
                no2 = int(input("NO2: "))
                so2 = int(input("SO2: "))
                
                alterar =(f"UPDATE indice SET MP10 = {mp10},MP2_5 = {mp2_5}, FMC = {fmc}, O3 = {o3}, CO = {co},NO2 = {no2},SO2 = {so2} WHERE id_indice = {id}")
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
                
                sql = (f"SELECT id_indice FROM indice")
                for i in cursor.execute(sql):
                                print (f"OPÇÃO: {i}")
                id = int(input("QUAL OPÇÃO VOCÊ DESEJA DELETAR?\nOPÇÃO: "))
                
                delete = (f"DELETE FROM indice WHERE id_indice = {id} ")
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
            

       
            
        
    
    
    
    
    

    


        
    



    