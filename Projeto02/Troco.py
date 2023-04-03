n_200 = 2
n_100 = 4
n_50 = 6
n_10 = 10
n_5 = 10
n_1 = 20
n_05 = 20

notas200 = 200 * n_200
notas100 = 100 * n_100
notas50 = 50 * n_50
notas10 = 10 * n_10
notas5 = 5 * n_5
notas1 = 1 * n_1
notas05 = 0.5 * n_05

soma_valor = 550
valor_pago = 600
troco = soma_valor - valor_pago
qtd_notas = 0

while valor_pago!=0:
    if troco < notas200:
