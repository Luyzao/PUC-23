total_entrevistado= 0
deseja_continuar= "s"
salarios_soma = 0
filhos_soma = 0
maior_salario = 0
qtd_pessoas_100 = 0
numero_filhos_entrevistado=0
salario_entrevistado=0
controle = 1
entrevistados = 1



while controle > 0:

   
   
    if deseja_continuar== "s" or deseja_continuar =="S":

        print(f"Entrevistado n°{entrevistados}")

        salario_entrevistado = float(input("Qual o salario? "))
        numero_filhos_entrevistado = int(input("Digite o numero de filhos "))
        entrevistados+=1
        total_entrevistado=entrevistados-1

        salarios_media= salarios_soma/total_entrevistado
        filhos_media=filhos_soma/total_entrevistado
        percentual_100=qtd_pessoas_100/total_entrevistado
        filhos_soma+=numero_filhos_entrevistado
        salarios_soma+=salario_entrevistado

        if salario_entrevistado <=100:
            
            qtd_pessoas_100+=1

        elif salario_entrevistado > maior_salario:
            maior_salario = salario_entrevistado

        deseja_continuar = input("Deseja ir para o proximo entrevistado? S/n ")

    elif deseja_continuar== "n" or deseja_continuar =="N":

        print(f"\n\n\nTotal de entrevistado: {total_entrevistado}")
        print(f"Média salarial: {salarios_media:.2f}")
        print(f"Média do numero de filhos: {filhos_media}")
        print(f"Maior salario: {maior_salario}")
        print(f"Percentual de pessoas com salario ate 100 reais:  {percentual_100:.2f} \n Pessoas ganhando 100 reais  = {qtd_pessoas_100} ") 
        break


