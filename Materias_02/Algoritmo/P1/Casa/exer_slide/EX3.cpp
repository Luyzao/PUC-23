#include <iostream>

using namespace std;

int main() 
{

    int a,b,c;
    float x, y, z;
    a = 5;
    b = 7 ;
    c =  -1 ;

    x = 4.5;
    y = 6.3;

    z = a * (x / (b+c*y)-x);

    cout<<"\nResultados:"<< z;
    cout<<endl<<endl<<endl;
    /*cout<<"\n\n\n";*/
    return 0;

}