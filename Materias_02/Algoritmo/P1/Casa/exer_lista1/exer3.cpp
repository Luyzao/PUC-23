#include <iostream>
using namespace std;
int main()
{

    float nota_a, nota_b, media;

    cout<<"insira as duas notas do aluno: ";cin>>nota_a>>nota_b;
    media=((nota_a*0.40)+(nota_b*0.60))/2;
    cout<<"A nota do aluno foi : "<<media;
    cout<<"\n\n";


    return 0;
}