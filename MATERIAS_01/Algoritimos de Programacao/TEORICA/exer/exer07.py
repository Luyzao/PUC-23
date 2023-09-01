#Maior menor entre 3 numeros

a = int(input("Insira o primeiro numero: "))
b = int(input("Insira o segundo numero: "))
c = int(input("Insira o terceiro numero: "))

if a>b and b>c:
    print(f"maior {a} menor {c}")
else:
    if a>c and c>b:
        print(f"maior {a} e menor {c}")
    else:
         if b>a and a>c:
            print(f"maior {b} e menor {c}")
         else:
             if b>c and c>a:
                print (f"maior {b} menor {a}")
             else: 
                 if c>a and a>b:
                    print(f'maior {c} menor {a}')
                 else:
                    if c>b and b>a:
                        print(f"maior {c} menor {a}")
                    else:
                        if a==b and b==c:
                            print("Tres iguais")
                        else:
                            if a==c: 
                                print(f'dois iguais')
                            else:
                                if a==b:
                                    print("dois numeros iguais")
                                else:
                                    print("todos iguais")