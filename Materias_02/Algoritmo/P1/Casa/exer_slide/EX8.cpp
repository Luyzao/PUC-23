#include <iostream>
using namespace std;

int main()
{
    int NUM;

    cout<<"Digite um DIGITO de 0 a 9: ";
    cin>> NUM;

    switch (NUM)
    {
    case 0: 
        cout<<NUM<<" ZERO";
        break;
    case 1:
        cout<<NUM<<" UM";
        break;
    case 2:
        cout<<NUM<<" DOIS";
        break;
    case 3:
        cout<<NUM<<"TRES";
        break;
    case 4:
        cout<<NUM<<"QUATRO";
        break;
    case 5:
        cout<<NUM<<"CINCO";
        break;
    case 6:
        cout<<NUM<<"SEIS";
        break;
    case 7:
        cout<<NUM<<"SETE";
        break;
    case 8:
        cout<<NUM<<"OITO";
        break;
    case 9: 
        cout<<NUM<<"NOVE";
        break;
    default: cout<<NUM<< "Invalido";

    }

    cout<<"\n\n";


    

    
    return 0;
}