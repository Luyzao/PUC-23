#include <iostream>
using namespace std;

int main() {

    int N, k;
    k=1;

    cout<<"\n\n\nInsira a qtd de numeros a serem exibidas ";cin>>N;

    while (k<=N)
        {
            cout<<" "<<k;
            k+=1;

        }

    cout<<"\n\n";
    return 0;
}