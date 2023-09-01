#include <iostream>
using namespace std;
int main()
{

    int a;

    cout<<"Insira um numero: ";cin>>a;

    if (a==0)
    {
        cout<<"Numero nulo!";

    }
    else if (a%2==0)
    {
        cout<<"Par";
    }
    else {
        cout<<"Impar";
    }
    return 0;
}