#Faça um programa em python para gerar os n primeiros termos da sequência: 1 1 2 3 5 8 13 21 34 55 89 …

fn1= 0
fn2=1

for i in range (10):
    n3=fn1+fn2
    fn1=fn2
    fn2=n3
    print(n3, end=' ')


