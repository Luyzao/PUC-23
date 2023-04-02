

while True:

    mp10 = int(input("MP10: "))
    mp2_5 = int(input("MP2,5: "))
    o3 = int(input("O3: "))
    co = int(input("CO: "))
    no2 = int(input("NO2: "))
    so2 = int(input("SO2: "))

    res = (mp10+mp2_5+o3+co+no2+so2)/6
    
    if mp10 < 0 or mp2_5 < 0 or o3 < 0 or co < 0 or no2< 0 or so2 < 0:
        print("ALGUM INDICE ESTA COM O VALOR INCOMPATIVEL \n REESCREVA OS DADOS POR FAVOR")
        continue
    else:
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
        OPC = int(input("VOCÊ QUER INSERIR OUTRA A MOSTRA?\n1.SIM\n2.NÃO QUERO SAIR DO PROGRAMA\n"))
        
        if OPC == 1:
            continue
        elif OPC == 2:
            break
        

