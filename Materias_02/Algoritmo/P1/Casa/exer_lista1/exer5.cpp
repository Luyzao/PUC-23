#include <iostream>
using namespace std;
#include <math.h>

int main()
{
    float x, resultado;

    do
    {
        cout<<"Insira um numero positivo: ";cin>>x;
    } while (x<0);

    resultado=sqrt(x);

    cout<<"O valor da raiz e: "<<resultado;





    return 0;
}