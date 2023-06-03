notas = []
N=int(input("ESCREVA QUANTOS ALUNOS QUE COLOCAR: "))
for i in range(N):
    nota1 = float(input("ESCREVA A NOTA: "))
    nota2 = float(input("ESCREVA A NOTA: "))
    print("\nPROXIMO ALUNO:")
    notas.append((nota1+nota2)/2)

for i in range(1,len(notas)+1):
    print(f"MEDIA DO {i}º ALUNO: {notas[i-1]}")
