#include <iostream>
using namespace std;

/*Construir um programa que faz a leitura de três números inteiros (a, b, c) e de uma
letra (pode ser maiúscula ou minúscula).
Usando o comando de seleção múltipla (switch/case), selecione de acordo com a letra:
A ou a: calcula x = a * ( b –c) / 2 + c e imprime o valor de x;
B ou b: calcula x = a * ( b + 2) + c/5 e imprime o valor de x;
C ou c: calcula x = (a – b) * ( c – b) / 2 e imprime o valor de x;
D ou d: calcula x = (a + b + c) / ( b + c) e imprime o valor de x;
E ou e: calcula x = a * a * a - ( b – c – a)/ 2 e imprime o valor de x;*/
int main()
{
    int a, b, c, x;
    char letra;

    cout<<"Insira tres numeros inteiros: "; cin>>a>>b>>c;
    cout<<"Escolha um modelo de conta abaixo: \nA ou a: calcula x = a * ( b –c) / 2 + c e imprime o valor de x; \nB ou b: calcula x = a * ( b + 2) + c/5 e imprime o valor de x;\n C ou c: calcula x = (a – b) * ( c – b) / 2 e imprime o valor de x;";
    cout<<"\nD ou d: calcula x = (a + b + c) / ( b + c) e imprime o valor de x; \n E ou e: calcula x = a * a * a - ( b – c – a)/ 2 e imprime o valor de x;";
    cout<<"\n\nEscolha uma letra: "; cin>>letra;

    switch(letra)
    {
        case 'a': case 'A':
            x= a * (b-c)/ 2 + c;
            cout<<"O resultado da conta foi :"<<x;
        break;
        
        case 'b': case 'B':
            x = a * ( b + 2) + c/5;
            cout<<"O resultado da conta foi :"<<x;
        break;

        case 'c': case 'C':
            x = (a - b) * ( c - b) / 2;
            cout<<"O resultado da conta foi: "<<x;
        break;

        case 'd': case 'D':
            x = (a + b + c) / ( b + c);
            cout<<"O resultado da conta foi: "<<x;
        break;

        case 'e': case 'E':
            x = a * a * a - ( b - c - a)/ 2;
            cout<<"O resultado da conta foi: "<<x;

        break;
        default:cout<<"Dado invalido!";
    }

    
    return 0;

}