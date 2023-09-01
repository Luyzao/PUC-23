#include <iostream>
using namespace std;
int main()
{
    int k, N, S =0;
    cout<<"\nSoma de N primeiros numeros pares\n";
    cout<<"Insira o valor de N: ";cin>>N;
    k=2;

    while (k<=2*N)

    {
        S+=k;
        k+=2;

    }
    cout<<"Soma: "<< S;
    cout<<"\n\n";




    return 0;
}