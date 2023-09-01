#include <iostream>
using namespace std;

/*ler três números inteiros DIFERENTES, imprimir qual o maior e qual o menor do
conjunto.*/

int main() 
{
    int a, b, c;

    cout<<"\n\n\n Maior e Menor";

    cout<<"\n\nInsira tres numeros inteiros a, b , c ";cin>>a>>b>>c;

    if (a>b && b>c)
        cout<<"Maior = "<<a<<"\tMenor = "<<c;
    else 
        if(a>c && c>b)
            cout<<"Maior = "<<a<<"\tMenor = "<<b;
    else
        if (b>a && c>a)
            cout<<"Maior = "<<b<<"\tMenor = "<<c;
    else
        if (b>c && c>a)
            cout<<"Maior = "<<b<<"\tMenor = "<<a;
    else
        if (c>a && a>b)
            cout<<"Maior = "<< c <<"\tMenor = "<<b;
    else
        cout<<"Maior = "<<c<<"\tMenor = "<< a;
    
    cout<<"\n\n\n";
    return 0 ;

}