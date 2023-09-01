#include <iostream>
using namespace std;

int main()

{
    int N;

    cout<<"Digite um numero inteiro: "; cin>> N;

    switch (N % 2)
    {
        case 0: cout<<"\n"<<N<<" --> PAR"; break;
        case 1: cout<<"\n"<<N<<"--> IMPAR";break;
    }
    cout<<"\n\n\n";
    return 0;

}