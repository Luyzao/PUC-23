#include <iostream>
using namespace std;
int main()
{
    float C, F;

    cout<<"Insira a temperatura em Fahrenheit: ";cin>>F;

    C=(5.0/9.0)*(F-32);
    cout<<"A temperatura em C e: "<<C;
    cout<<"\n\n";
    return 0;
}