#include <iostream>
using namespace std;

int main()
{
    int x;

    cout<< "\n\nInsira um numero: "; cin>>x;

    switch (x%2) {
        case 0: cout<<"O numero "<< x <<" e par!";
        break;
        case 1: cout<<"O numero "<< x <<" e impar!";
        break;
    }

    cout<<"\n\n";
    return 0;
}