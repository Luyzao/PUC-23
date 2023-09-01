#include <iostream>
using namespace std;

int main()
{
    int NUM;
    cout<<"Digite um DIGITO de 0 a 9: ";
    cin>>NUM;

    if (NUM == 0)
        cout<<"0 --> "<<"ZERO";
    else if (NUM == 1)
        cout<<"1 --> "<<"UM";
    else if (NUM == 2)
        cout<<"2 --> "<<"DOIS";
    else if (NUM == 3)
        cout<<"3 --> "<<"TRES";
    else if (NUM == 4)
        cout<<"4 --> "<<"QUATRO";
    else if (NUM == 5)
        cout<<"5 --> "<<"CINCO";
    else if (NUM == 6)
        cout<<"6 --> "<<"SEIS";
    else if (NUM == 7)
        cout<<"7 --> "<< "SETE";
    else if (NUM == 8)
        cout<<"8 --> "<<"OITO";
    else if (NUM == 9)
        cout<<"9 --> "<<"NOVE";
    else cout<<"Invalido";

    return 0;
}