#include <iostream>
using namespace std;

/*Calcular a área do quadrilátero e imprimir se quadrado ou retângulo. O programa deverá ter como
dados de entrada: base e altura. Além de imprimir o valor da área calculado, imprimir a mensagem se
quadrado ou retângulo.*/

int main()

{
    float a, b, c;
    cout<<"\n\n\tArea do quadrilatero";
    cout<<"\n\nInsira o valor da base: "; cin>>a;
    cout<<"\nInsira o valor da altura: "; cin>>b;

    c = a * b;

    if ( a == b )
        cout<<"\nArea do quadrado = "<<c<<endl<<endl;
    
    else
        cout<<"\n Are do Retangulo = "<<c<<endl<<endl;

    return 0 ;


}