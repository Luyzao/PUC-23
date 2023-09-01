# Função para calcular o fatorial de um número
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Leitura do número inteiro
n = int(input("Digite um número inteiro: "))

# Verificação se o número é positivo
if n < 0:
    print("Erro: não é possível calcular o fatorial de um número negativo.")
else:
    # Cálculo do fatorial
    fat = fatorial(n)

    # Impressão do resultado
    print("{}! = {}".format(n, fat))
