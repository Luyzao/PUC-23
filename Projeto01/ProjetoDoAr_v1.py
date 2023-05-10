import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_9")
import sys
import functools
try:
        
    conexao=cx_Oracle.connect(user='ADM',password='bolinho',dsn='localhost/xe')
       

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


                soma = (f"SELECT SUM(MP10 + MP2_5 + FMC + O3 + CO + NO2 + SO2) FROM indice WHERE id_indice = {id}")
                for i in cursor.execute(soma):
                    res = int(''.join(map(str, i)))
                    print (res)
                
                                
                    #EFEITOS
                    
                if res >= 0 and res <= 40:
                    print("Qualidade do ar está BOA\nEfeitos: Nenhum")
                elif res >= 41 and res <=80:
                    print("Qualidade do ar está MODERADA\nEfeitos: Pessoas de grupos sensiveis (crianças, idosos e \npessoas com doenças respiratórias e cardiacas) \npodem apresentar sintomas com tosse seca e \ncansaço. A população, em geral, não é afetada.")
                elif res >= 81 and res <=120:
                    print("Qualidade do ar está RUIM\nEfeitos: Toda a população pode apresentar sintomas como \ntosse seca, cansaço, ardor nos olhos, nariz e \ngarganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e \ncardíacas) podem apresentar efeitos mais sérios na saúde.")
                elif res >= 121 and res <= 200:
                    print("Qualidade do ar está MUITO RUIM\nEfeitos: Toda a população pode apresentar agravamento dos \nsintomas como tosse seca, cansaço, ardor nos olhos, \nnariz e garganta e ainda falta de ar e respiração \nofegante. Efeitos ainda mais graves à saúde de \ngrupos sensíveis (crianças, idosos e pessoas com \ndoenças respiratórias e cardíacas).")
                elif res > 200:
                    print("Qualidade do ar está PÉSSIMO\nEfeitos: Toda a população pode apresentar sérios riscos de \nmanifestação de doenças respiratórias e \ncardiovasculares. Aumento de mortes prematuras \nem pessoas de grupos sensíveis.")         
                OPC = int(input("VOCÊ QUER VOLTAR PARA O MENU?\n1.SIM\n2.NÃO QUERO SAIR DO PROGRAMA\n"))
                       
       
                            
                if(OPC == 1):

                    continue
                                
                elif OPC == 2:
                     sys.exit(0)
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
            

       
            
        
    
    
    
    
    

    


        
    



    