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

        controle = 0
        
        while controle == 0:
            
            opc = int(input("QUAL INDICE VOCÊ QUER VER A MEDIA? \n1.MP10\n2.MP2,5\n3.O3\n4.CO\n5.NO2\n6.SO2\n7.FECHAR PROGRAMA\nESCREVA O NUMERO EQUIVALENTE AO INDEICE DESEJADO:  "))
            
            if opc < 7:
            
                if opc == 1:
                    opc = "mp10"
                elif opc == 2:
                    opc = "mp2_5"
                elif opc == 3:
                    opc = "o3"
                elif opc == 4:
                    opc = "co"
                elif opc == 5:
                    opc = "no2"
                elif opc == 6:
                    opc = "so2"
            
         
                cursor = conexao.cursor()
                
                soma = (f"SELECT SUM({opc}) FROM indice")
                conta = ("SELECT COUNT(*) FROM indice")
                for i in cursor.execute(soma):
                    res = int(''.join(map(str, i)))
                    
                for i in cursor.execute(conta):
                    quant = int(''.join(map(str, i)))
                    

                media = res/quant
                print(f"\nA media do indice {opc} é {media}\n\n")
                
                if media >= 0 and media <= 40:
                    print("Qualidade do ar está BOA\nEfeitos: Nenhum")
                elif media >= 41 and media <=80:
                    print("Qualidade do ar está MODERADA\nEfeitos: Pessoas de grupos sensiveis (crianças, idosos e \npessoas com doenças respiratórias e cardiacas) \npodem apresentar sintomas com tosse seca e \ncansaço. A população, em geral, não é afetada.")
                elif media >= 81 and media <=120:
                    print("Qualidade do ar está RUIM\nEfeitos: Toda a população pode apresentar sintomas como \ntosse seca, cansaço, ardor nos olhos, nariz e \ngarganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e \ncardíacas) podem apresentar efeitos mais sérios na saúde.")
                elif media >= 121 and media <= 200:
                    print("Qualidade do ar está MUITO RUIM\nEfeitos: Toda a população pode apresentar agravamento dos \nsintomas como tosse seca, cansaço, ardor nos olhos, \nnariz e garganta e ainda falta de ar e respiração \nofegante. Efeitos ainda mais graves à saúde de \ngrupos sensíveis (crianças, idosos e pessoas com \ndoenças respiratórias e cardíacas).")
                elif media > 200:
                    print("Qualidade do ar está PÉSSIMO\nEfeitos: Toda a população pode apresentar sérios riscos de \nmanifestação de doenças respiratórias e \ncardiovasculares. Aumento de mortes prematuras \nem pessoas de grupos sensíveis.")         
                
                controle2 = 0
                
                while controle2 == 0:
                    
                    opc = input("QUER CONTINUAR? (SIM: S ou s / NÃO: N ou n)")
                    
                    if opc == "n" or opc == "N":
                        print("ADEUS...")
                        controle2 = 1
                        controle = 1
                        
                    
                    if opc == "s" or opc == "S":
                        controle2 = 1
                        
            elif opc == 7:
                controle = 1   
            
            else:
                print("DADO INVALIDO\n")
