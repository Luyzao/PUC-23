#include <iostream>
#include <math.h>
using namespace std;
int main()
{

    float X, Y, resultado;
    
    do{
    cout<<"Insira o valor de x: "; cin>>X;
    cout<<"Insira o valor de y: "; cin>>Y;
    } while(X<0 && Y<0);

    
    resultado = pow(X,Y);

    cout<<"O resultado e: "<<resultado;

    return 0;
}