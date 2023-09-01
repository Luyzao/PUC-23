#include <iostream>
using namespace std;
int main()
{
    /*Exemplo 3: construir um programa que calcula e imprime o valor do seguinte somatório, onde N deve ser lido*/

    float num, den, N, s;
    num=1;
    den=1;
    s=0;
    cout<<"Insira o valor de N: "; cin>>N;

    while (den<=N)
    {
        s+=num/den;
        den+=1;

    }
    cout<<"O valor da soma e:"<<s;
    cout<<"\n";


    return 0;
}