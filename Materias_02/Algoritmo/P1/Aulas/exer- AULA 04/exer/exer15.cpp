#include <iostream>
using namespace std;
int main()
{

    int k, N, X;

    cout<<"\n\nInsira o numero de multiplos: ";cin>>N;

    cout<<"Multiplos de 5\n\n";
    X=5;
    /*INICIO, CONDICAO DE PARADA, PASSO (ADICIONA 1 EM 1)*/
    for(k=1; k<=N; k++)
    {
        cout<<" "<<X;
        X+=5;
    }
    cout<<"\n\n";

    return 0;
}