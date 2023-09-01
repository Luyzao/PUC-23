#include <iostream>
using namespace std;

int main()
{
    float nota;
    do {
        cout<<"Nota: ";
        cin>> nota;

    }
    while (nota<0 || nota >10);
    cout<< ">>>Nota do aluno = " <<nota<<endl;
    
    return 0 ;
}