#include <iostream>
using namespace std;
int main()
{
    float x,y,z;
    
    cout<<"Insira os lados do triangulo: ";cin>>x>>y>>z;

    if (x<y+z && y<x+z && z<x+y)
    {
        if (x==y && y==z)
        {
            cout<<"\n Triangulo equilatero\n";
            cout<<"\n triangulo isoceles\n";
        }
        else if (x==y || z==y || x==z )
        {
            cout<<"\n\nTriangulo isoceles\n";
        }
        else 
        {
            cout<<"Triangulo escaleo\n";
        }

    }
    else{
        cout<<"\nNao é um triangulo";
    }
    return 0;
}