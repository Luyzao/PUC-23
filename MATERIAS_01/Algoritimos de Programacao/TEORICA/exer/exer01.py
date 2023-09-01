#Exercicio exemplo Angela

nome="Angela"
sobrenome="Mariano"

print(f"Comprimento = {len(nome)}")
print(f"procura de 'ge' em Angela = {'ge' in nome}" ) #Retorna se ge esta em angela
print(f"procura de 'ge' em Angela = {'GE' in nome}" ) #Retorna se GE maisculo esta em angela
print(f"X não esta no sobrenome {'x' not in sobrenome} ") #x nao esta no sobrenome - verdade
print(f"X esta no sobrenome {'x' in sobrenome}") #x esta neste sobrenome - mentira

print( nome+" "+sobrenome)
