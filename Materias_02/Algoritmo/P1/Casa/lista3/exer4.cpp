#include <iostream>
using namespace std;
int main()
{
    float nota1, nota2, resultado,p1, p2;

    cout<<"\nInsira a nota 1: ";cin>>nota1;
    cout<<"\nInsira a nota 2: "; cin>>nota2;
    cout<<"\nInsira o p1 em %: "; cin>> p1;
    cout<<"\nInsira o p2 em %: "; cin>> p2;

    resultado = (((nota1*p1)+(nota2*p2))/100);

    if (resultado >=7 && resultado <10)
    {
        cout<<"\nAprovado"<<resultado;
        cout<<"\n";

    }
    else if (resultado <7)
    {
        cout<<"\nReprovado"<<resultado;
        cout<<"\n";
    }
    else if (resultado == 10)
    {
        cout<<"\nAprovado com distincao!"<<resultado;
        cout<<"\n";
    }
    else
    {
        cout<<"Notas invalidas!";
        cout<<"\n";
    }
    return 0;
}