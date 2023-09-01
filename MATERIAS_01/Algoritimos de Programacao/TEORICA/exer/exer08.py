# resolução de outra forma

a = int(input("Insira o numero "))
b = int(input("Insira o segundo numero "))
c = int(input("Insira o terceiro numero "))

if a>b>c:
    print(f'a é maior {a} c é menor  {c}')
elif a>c>b:
    print(f'a é maior {a} b é menor {b}')
elif b>a>c:
    print(f'b é maior {b} c é menor {c}')
elif b>c>a:
    print(f'b é maior {b} a é menor {c}')
elif c>a>b:
    print(f'c é maior {c} b é menor {b}')
elif c>b>a:
    print(f'c é maior {c} a é menor {a}')
elif a==b==c:
    print(f'os tres numeros sao iguais {a,b,c}')
elif a==b:
    print(f'a e b são iguais {a,b}')
elif a==c:
    print(f'a e c são iguais {a,c}')
elif b==c:
    print(f'b e c são iguais {b,c}')