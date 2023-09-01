#include <iostream>
using namespace std;
int main()
{
    int k, N, X;
    k=5;
    N=0;
    X=5;
    cout<<"Multiplos de 5";
    cout<<"\nInsira quantos multiplos de 5 deseja exibir: ";cin>>N;
    /*Caso eu digite 5 ele vai fazer 5 vezes o loop*/
    for (k=5; k<=5*N; k+=5)
        cout<<" "<<k;
    cout<<"\n\n";
    return 0;
}