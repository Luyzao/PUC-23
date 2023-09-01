#include <iostream>
using namespace std;
int main()
{
    int divisor, dividendo, quociente, resto;
    char sn;

    do{ 
        cout<<"\n\n Calcular o  Quociente e Resto\n";
        cout<<"------------------------------------------";
        cout<<"\nInsira o dividendo: ";cin>>dividendo;

        do{
            cout<<"Divisor: "; cin>>divisor;
        } while(divisor<10 || divisor>100 ); /*nao tem como um mesmo numero ser duas coisas ao mesmo tempo*/

        quociente = dividendo/divisor;
        resto = dividendo%divisor;
        cout<<"\n\n"<<"Divisor = "<<divisor<<" / "<< "\nDividendo = "<<dividendo<<" \nQuociente = "<<quociente<< "\nResto = "<<resto;

        cout<<"\nDeseja efetuar a conta novamente?";
        getchar(); cin>>sn;
    } while(sn=='s' || sn=='S');
    cout<<"\n Obrigada por usar o programa";
    

    return 0;
}