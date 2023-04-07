
nota = -1
while nota < 0 or nota > 10:
    try:
        nota = int(input("Informe a nota entre 0 e 10: "))
        print("A nota foi:", nota)
        break
    except:
        print("Valor inválido")
        