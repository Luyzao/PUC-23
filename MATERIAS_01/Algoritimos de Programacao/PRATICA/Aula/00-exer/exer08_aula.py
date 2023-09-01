#calcular a area de um quadrilatero

print("ENTRADA DE DADOS")
base=float(input("Base"))
altura=float(input("Altura"))

area= base*altura

if base==altura:
    print(f"Area do Quadrado = {area:.2f}")
else:
    print(f"Area do Retangulo = {area:.2f}")
