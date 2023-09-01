cod_voo = "123"
voo_inf = ['CAMPINAS/SAOPAULO','CAMPINAS','SAO PAULO','2',['RIO DE JANEIRO, MINAS GERAIS']]

print('-' * 150)
print(f"| {'Codigo':^10} | {'Nome VOO':^20} | {'Origem':^30} | {'Destino':^20} | {'Qtd. Escalas':^20} | {'Cid. Escalas':^32} |")
print('-' * 150)
print(f'| {cod_voo:^10} | {str(voo_inf[0]):^20} | {str(voo_inf[1]):^30} | {str(voo_inf[2]):^20} | {str(voo_inf[3]):^20} | {str(voo_inf[4]):^32} |')
print('-' * 150)