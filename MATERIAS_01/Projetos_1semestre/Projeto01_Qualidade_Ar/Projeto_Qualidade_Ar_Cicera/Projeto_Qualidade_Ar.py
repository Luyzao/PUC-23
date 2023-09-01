##Projeto da disciplina projeto integrador I, que visa a construcao de um programa que atraves da insercao de valores 
#classifique e indique a qualidade do ar

while True:

    print("INSIRA AS AMOSTRAS")
    mp10 = int(input("MP10: "))
    mp2_5 = int(input("MP2,5: "))
    o3 = int(input("O3: "))
    co = int(input("CO: "))
    no2 = int(input("NO2: "))
    so2 = int(input("SO2: "))

    res = (mp10 +mp2_5 +o3 +co +no2 +so2 ) /6

    if mp10 < 0 or mp2_5 < 0 or o3 < 0 or co < 0 or no2 < 0 or so2 < 0:
        print("ALGUM INDICE ESTA COM O VALOR INCOMPATIVEL \n REESCREVA OS DADOS POR FAVOR")
        continue
    else:
        if mp10 > 250 or mp2_5 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 >800:
            print \
                ("Qualidade do ar está PÉSSIMO\nEfeitos: Toda a população pode apresentar sérios riscos de \nmanifestação de doenças respiratórias e \ncardiovasculares. Aumento de mortes prematuras \nem pessoas de grupos sensíveis.")
        elif 150 < mp10 <= 250 or 75 < mp2_5 <= 125 or 160 < o3 <= 200 or 13 < co <= 15 or 320 < no2 <= 1130 or 365 < so2 <= 800:
            print \
                ("Qualidade do ar está MUITO RUIM\nEfeitos: Toda a população pode apresentar agravamento dos \nsintomas como tosse seca, cansaço, ardor nos olhos, \nnariz e garganta e ainda falta de ar e respiração \nofegante. Efeitos ainda mais graves à saúde de \ngrupos sensíveis (crianças, idosos e pessoas com \ndoenças respiratórias e cardíacas).")
        elif 100 < mp10 <= 150 or 50 < mp2_5 <= 75 or 130 < o3 <= 160 or 11 < co <= 13 or 240 < no2 <= 320 or 40 < so2 <= 365:
            print \
                ("Qualidade do ar está RUIM\nEfeitos: Toda a população pode apresentar sintomas como \ntosse seca, cansaço, ardor nos olhos, nariz e \ngarganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e \ncardíacas) podem apresentar efeitos mais sérios na saúde.")
        elif 50 < mp10 <= 100 or 25 < mp2_5 <= 50 or 100 < o3 <= 130 or 9 < co <= 11 or 200 < no2 <= 240 or 20 < so2 <= 40:
            print \
                ("Qualidade do ar está MODERADA\nEfeitos: Pessoas de grupos sensiveis (crianças, idosos e \npessoas com doenças respiratórias e cardiacas) \npodem apresentar sintomas com tosse seca e \ncansaço. A população, em geral, não é afetada.")
        elif mp10 <= 50 or mp2_5 <= 25 or o3 <= 100 or co <= 9 or no2 <= 200 or so2 <= 20:
            print \
                ("Qualidade do ar está BOA\nEfeitos: Nenhum")
        OPC = int(input("VOCÊ QUER INSERIR OUTRA A MOSTRA?\n1.SIM\n2.NÃO QUERO SAIR DO PROGRAMA\n"))

        if OPC == 1:
            continue
        elif OPC == 2:
            break