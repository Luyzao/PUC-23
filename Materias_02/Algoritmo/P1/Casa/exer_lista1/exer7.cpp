#include <iostream>
using namespace std;
int main()
{
    float a, b, c, d, e, f, x, y;

    cout<<"\nInsira o valor de a: ";cin>>a;
    cout<<"\nInsira o valor de b: ";cin>>b;
    cout<<"\nInsira o valor de c: ";cin>>c;
    cout<<"\nInsira o valor de d: ";cin>>d;
    cout<<"\nInsira o valor de e: ";cin>>e;

    x=((c*e)-(b*f))/((a*e)-(b*d));
    y =((a*f)-(c*d))/((a*e)-(b*d));

    cout<<"O resultado para a conta x e: "<<x;
    cout<<"\nO resultado para a conta y e : "<<y;
    cout<<"\n\n";

    return 0;
}