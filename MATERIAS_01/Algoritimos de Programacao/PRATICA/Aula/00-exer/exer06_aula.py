# 5 Leia o salario mensal atual de um funcionario e o percentual de reajuste e determine o valor do novo salario
print("")
salario=float(input("Insira o salario mensal atual: "))
ajuste=float(input("Insira o valor do aumento em porcentagem: Exemplo 15: "))

aumento=salario*(ajuste/100)
soma= aumento+salario

print(f"O salario de R${salario:.2f}, passa a R${soma:.2f} apos o aumento de R${aumento:.2f}")