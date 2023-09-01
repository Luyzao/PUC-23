#6. A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados
#sobre o salário e número de ﬁlhos. A prefeitura deseja saber:
#a. média do salário da população;
#b. média do número de ﬁlhos;
#c. maior salário;
#d. percentual de pessoas com salário até R$100,00.

entrevistados = int(input(" Digite o numero de entrevistados "))

soma_salario=0
soma_filhos=0
maior_salario=0
salario_100=0
filhos= 0
salario = 0
percentual=0

for i in range (1,entrevistados+1): 

    print(f"\nEntrevistado numero: {i}")
 
    salario = float(input("Digite o salario: R$"))
    filhos = int(input("Digite a quantidade de filhos: "))
    soma_filhos+=filhos
    soma_salario+=salario

    if salario <=100:
        salario_100+=1        
        entrevistados = -1


    if maior_salario<salario:
        maior_salario= salario

        
media_salario = (soma_salario)/entrevistados
media_filhos = (soma_filhos)/entrevistados
percentual = ((salario_100*100)/entrevistados)



print(f"\n\nO numero total de entrevistados foi {entrevistados}")
print(f"A media do salario da população é de {media_salario}")
print(f"A media de filhos é de {media_filhos}")
print(f"O maior salario foi de {maior_salario} reais")
print(f"O percentual de pessoas com salario até 100 reais é de {percentual} %")



