#include <iostream>
using namespace std;
int main()
{
    /*1. Construir um programa que imprime os múltiplos de 5 menores ou iguais à 100, iniciando em 5. Utilizar o
    comando for.*/

    int k;


    cout<<"Multiplos de 5\n";
    /*valor de inicio, valor final, passo*/
    for (k = 5; k<=100; k+=5)
    cout<<" "<<k;

    cout<<"\n\n";


    return 0;
}