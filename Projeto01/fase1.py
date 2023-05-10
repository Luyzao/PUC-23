controle = 0
while controle == 0:
    print('-'*40)
    print("Insira as amostras coletadas a seguir:")
    print('-'*40)
    mp10 = int(input("• MP10: "))
    print('-'*40)
    mp2_5 = int(input("• MP2,5: "))
    print('-'*40)
    o3 = int(input("• O3: "))
    print('-'*40)
    co = int(input("• CO: "))
    print('-'*40)
    no2 = int(input("• NO2: "))
    print('-'*40)
    so2 = int(input("• SO2: "))
    print('-'*40)

    res = (mp10 +mp2_5 +o3 +co +no2 +so2 )/6

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
                
        controle1 = 0
                
        while controle1 == 0   :
            OPC =int(input("\nDeseja inserir outra amostra?\n• Digite 1, se sim...\n• Ou digite 2, se não.\n"))

            if OPC == 1:
                
                controle1 = 1
            elif OPC == 2:
                controle =1
                controle1 = 1