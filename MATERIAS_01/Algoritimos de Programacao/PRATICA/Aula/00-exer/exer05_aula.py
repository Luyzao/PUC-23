## formatacao

nome= "Ana"
idade= float(330) 
peso= float(49.564)
numero=1000000000000000.000000000000000

print(f"\n{nome:^40}") #centralizado com 40 caracteres no total
print(f"{numero:.5f}") #5 casas decimais 
print(f"{numero:4} :4")#uma casa decimal
print(f"{nome:20} esse aqui")#20espaços de distancia
print(f"{idade:2}")#uma casa decimal
print("")
print("")
print("")

print(f"|{nome:15}|")#"Tamanho"
print(f"1|{nome} {idade}")
# {:<xx} formatacao de tamanho e a esquerda e para o float o numero de casas decimais
print(f"2|{nome:<40}|{idade:<20}|") #DIREITA vinte espaços, contando com as caractes do nome a direita

print(f"7|{nome:<50}|{idade:<15}|")
print(f"3|{nome:40}|{idade:.16f}|")
print(f"4|{nome:>40}|{idade:>20}|") # a direita

print(f"5|{nome:^10}|{idade:<20}|") #formatacao de tamanho e centralizado | vinte espaços 
print(f"6|{nome:^50}|") #coloca o nome no meio dos 50 espaços