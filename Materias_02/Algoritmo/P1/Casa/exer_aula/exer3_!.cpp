#include <cmath>
#include <iostream>
using namespace std;

int main()
{
    int a,b,c;
    float delta, x1,x2;
    cout<<" Digite os coeficientes da equacao do 2o. grau: ax2 + bx + c";
    cin>>a>>b>>c;

    if(a !=0){
        delta = b*b - 4*a*c;
        if (delta > 0){
            x1 = (-b + sqrt(delta)) / (2*a);
            x2 = (-b - sqrt(delta)) / (2*a);
            cout<<" Raizes: "<< x1 << " e " << x2<<endl;
        }
        else
            if(delta == 0){
                x1 = -b  / (2*a);
                cout<<" Raiz: "<< x1 <<endl;
            }
            else cout<<" Nao tem raiz real."<<endl;
      }
      else cout<<" Divisao por zero.";

    cout << endl;
    return 0;
}