#6. A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados
#sobre o salário e número de ﬁlhos. A prefeitura deseja saber:
#a. média do salário da população;
#b. média do número de ﬁlhos;
#c. maior salário;
#d. percentual de pessoas com salário até R$100,00.

print("\n\nDigite -1 para encerrar a qualquer momento\n\n")

#variaveis
salario_total=0
filhos_total=0
qtd_pessoas_100=0
salario=0
filhos=0
qtd_pessoas= 0
percentual_pessoas=0
maior_salario=0

while True:
    
    
    qtd_pessoas+=1
    print(f"Entrevistado numero {qtd_pessoas}")
    salario=(float(input("Insira o salario: ")))

    if salario ==-1:
        qtd_pessoas-=1
        break

    filhos = (int(input("Insira o numero de filhos: ")))
    salario_total +=salario
    filhos_total +=filhos    

    #c. maior salário;
    if maior_salario<salario:
        maior_salario= salario

    #d. percentual de pessoas com salário até R$100,00.
    if salario<=100:
        qtd_pessoas_100+=1


#processamento
    
#a. média do salário da população;
media_salario = (salario_total)/qtd_pessoas
#b. média do número de ﬁlhos;
media_filhos = (filhos_total)/qtd_pessoas
#d. percentual de pessoas com salário até R$100,00.
percentual_pessoas = ((qtd_pessoas_100*100)/qtd_pessoas)


#saida
if percentual_pessoas >0:
    print(f"\n\nPercentual de pessoas com salario ate 100 reais é de {percentual_pessoas:.0f}%")
else:
    print(f"\n\nTodos os entrevistados tem o salario maior que 100 reais")

print(f"Numero de entrevistados {qtd_pessoas}")
print(f"Media do salario da população  {media_salario}")
print(f"Media do numero de filhos {media_filhos}")
print(f"Maior salario {maior_salario}")
