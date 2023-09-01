/* Construir um programa para calcula o volume da esfera de raio r. O programa deve ler o valor do raio e imprimir o valor do volume*/

#include <iostream>
#include <math.h>
#define PI 3.14159 /*Adiciona o valor fixo*/
using namespace std;

int main()
{
    float r, V;

    cout<<"\n\tCalculo de volume de esfera";
    cout<<"\n\nInsira o valor do r = "; cin>> r;

    V=(4 * PI * pow(r,3))/3; /*M_PI=PI*/
    cout<<"\n Volume = "<<V;

    cout<<"\n\n";

    return 0;
}