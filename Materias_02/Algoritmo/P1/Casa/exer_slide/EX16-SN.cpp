#include <iostream>

using namespace std;

/*Comandos repetitivos aninhados*/

int main()
{
    int dividendo, divisor, quociente, resto;
    char sn;

    cout<<"Insira o numero para ser dividido: "; cin>>dividendo;

    do{

        cout<<"Insira o Divisor: "; cin>>divisor;

    } 
    while (sn=='s' || sn=='S');
    cout<< " ";

    return 0;
}