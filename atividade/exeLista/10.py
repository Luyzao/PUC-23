lista = [2,2,3,4,5,6,7,8,9,10]
soma = 0
mult = 1
for i in range(len(lista)):
   
    soma += lista[i]

    mult *= lista[i]

print(f"SOMA: {soma}\nMULTIPLICAÇÃO: {mult}\nNUMEROS: {lista}")