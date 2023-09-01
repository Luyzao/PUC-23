#include <iostream>
using namespace std;
int main()
{

    char letra1, letra2;
    int k=1,N=0;


    cout<<"Qtas vezes?: ";cin>>N;

    while (k<=N)

    {
    cout<<"\n\nInsira uma letra: ";cin>>letra1;

    cout<<"Letra lida: "<<letra1;
    letra2=toupper(letra1);
    cout<<"\nLetra Maiuscula: "<<letra2;
    letra2=tolower(letra1);
    cout<<"\nLetra Minuscula: "<<letra2;
    cout<<"\n\n\n";
    k++;
    }

    return 0;
}