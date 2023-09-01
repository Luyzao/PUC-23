par = []
impar= []

N = int(input("ESCREVA QUANTOS NUMERO DESEJA COLOCAR: "))
for i in range(N):
    num = int(input("ESCREVA UM NUMERO: "))
    if num %2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"NUMEROS PARES: {par}\nNUMEROS IMPAR: {impar}")