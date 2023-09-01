#include <iostream>
using namespace std;
int main()
{
    int a, b, c;

    cout<<"Insira os valores de a e b: "; cin>>a>>b;

    if (a==b)
    {
        c=a+b;
        cout<<"Soma : O valor é "<<c;
        cout<<"\n\n";

    }

    else
    {
        c=a*b;
        cout<<"Multiplicacao: O valor é: "<<c;
        cout<<"\n\n";
    }
    return 0;
}