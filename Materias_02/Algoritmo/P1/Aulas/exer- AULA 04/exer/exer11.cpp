#include <iostream>
using namespace std;
int main()
{
    int N, x,s=0, k=1;
    /*Exemplo2: calcular o somatório de N números inteiros, lidos, pela variável X. O valor de N, também, deverá ser lido.*/
    cout<<"\n Insira o valor de numeros a serem calculados: ";cin>>N;

    while(k<=N)

    {
        cout<<"\nInsira o "<<k<<" numero: "; cin>>x;
        s+=x;
        k++;

    }
    cout<<"A soma dos "<<N<<" numeros digitados e: "<<s;
    cout<<"\n";
    
    return 0;
}