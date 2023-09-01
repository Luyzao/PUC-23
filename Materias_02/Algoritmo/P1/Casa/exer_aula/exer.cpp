#include <iostream>
using namespace std;
int main()
{
    float numero1,numero2,resultado;
    char sn, oper,e;
    
    cout<<"\n\nCalculadora\n\n";

    sn = 's';
    e = '=';

    do 
    {
        cin>>numero1>>oper>>numero2;

        switch(oper){
            case '+': 
                resultado = numero1 + numero2;
                cout << numero1 << oper << numero2 << e << resultado;
                break;
            case '-':
                resultado = numero1-numero2;
                cout<<numero1<<oper<<numero2<<e<<resultado;
                break;
            case '*':
                resultado = numero1*numero2;
                cout<<numero1<<oper<<numero2<<e<<resultado;
                break;
            case '/':
                if (numero2!=0){
                
                    resultado = (numero1/numero2);
                    cout<<numero1<<oper<<numero2<<e<<resultado;
                    
                } else{
                    cout<<"Erro: Divisao por zero";
                }
                break;
            default: 
                cout<<"Operador invalido! ";
                break;
            
        }
        cout<<"\n\nDeseja continuar? Ss/Nn";cin>>sn;
    


    } while (sn=='s' || sn=='S');

    return 0;
}