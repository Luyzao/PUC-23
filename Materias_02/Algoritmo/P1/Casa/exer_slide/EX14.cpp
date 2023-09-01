#include <iostream>

using namespace std;

/* Imprimir os N primeiros numeros naturais*/

int main()
{   
    int x, N;
    x=1; /*apartir de zero*/
    cout<<"Insira o numero de numeros a serem mostrados: "; cin>>N;

    while (x<=N)
    {
        cout<<" "<<x;
        x+=1;
        
    }

    cout<<"\n\n";
    
    return 0;
}