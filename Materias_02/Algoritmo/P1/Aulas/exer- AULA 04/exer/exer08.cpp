#include <iostream>
using namespace std;
int main()
{
    /*Os 10 primeiros numeros naturais e sua somatoria*/ 

    int N,k,s;
    N=0;
    k=1;
    s=0;

    cout<<"\n Insira quantos numeros devem ser exibidos: ";cin>>N;
    cout<<"Os "<<N<<" primeiros numeros sao: \n";

    while(k<=N)
    {
        
        cout<<" "<<k;
        s+=k;
        k++;

    }
    cout<<"\nA soma desses numeros e: "<<s;
    cout<<" \n";

    return 0;
}