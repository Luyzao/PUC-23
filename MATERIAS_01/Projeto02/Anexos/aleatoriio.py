
controle = 0

while controle == 0:

    OPC = int(input("DESEJA ALGO?\n (1.S ou 2.N)"))
    
    if OPC == 1:
        print("OLA")
        controle = 1
        
    elif OPC == 2:
        print("ADEUS")
        controle = 1

    else:
        print("VALOR INVALIDO\n\n")