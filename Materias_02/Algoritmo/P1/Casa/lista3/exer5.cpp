#include <iostream>
using namespace std;
int main()
{
    float salario_atual, salario_reajuste;
    
    cout<<"\n Insira o valor do salario: "; cin>>salario_atual;
    if(salario_atual<500)
    {
        salario_reajuste = (salario_atual*0.15) +salario_atual;
        cout<<"O funcionario vai receber 15%, sendo seu novo salario: "<<salario_reajuste;
        cout<<"\n\n";
    }
    else if (salario_atual>=500 && salario_atual<=1000) {
        salario_reajuste = (salario_atual*0.10) +salario_atual;
        cout<<"O funcionario vai receber 10%, sendo seu novo salario: "<<salario_reajuste;
        cout<<"\n\n";

    }
    else if (salario_atual>1000)
    {
        salario_reajuste = (salario_atual*0.05) +salario_atual;
        cout<<"O funcionario vai receber 5%, sendo seu novo salario: "<<salario_reajuste;
        cout<<"\n\n";

    }
    else{
        cout<<"Comando Invalido";
    }
    return 0;
}