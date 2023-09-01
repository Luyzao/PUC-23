# Exercicio 03 - Condicao if
#   calcule de are de quadrilatero

base = float(input("Insira a base da area: "))
altura = float(input("Insira a altura da base: "))

#calculo da area

area=base*altura

if base ==altura:
    print(f'Area do quadrado = {area:.2f}')

else: 
    print(f'Area do retangulo = {area:.2f}')
