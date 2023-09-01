#include <iostream>
using namespace std;

/*verifica se caractere digitado é uma das vogais - se for, escrever se “minúscula” ou “maiúscula” se não for vogal, escrever mensagem: “outro caractere”*/



int main()

{
    char caracter;
    cout<<"\n\n Insira um caracter: ";cin>>caracter;

    switch (caracter) {
        case 'a': cout<<"Vogal Minuscula"; break;
        case 'e': cout<< "Vogal Minuscula"; break;
        case 'i': cout<< "Vogal Minuscula"; break;
        case 'o': cout<< "Vogal Minuscula"; break;
        case 'u': cout<< "Vogal Minuscula"; break;

        case 'A': cout<<" Vogal Maiuscula"; break;
        case 'E': cout<<"Vogal Maiuscula"; break;
        case 'I': cout<<"Vogal Maiuscula"; break;
        case 'O': cout<<"Vogal Maiuscula"; break;
        case 'U': cout<<"Vogal Maiuscula"; break;
        default: cout<<"Outro caracter";

    } 

    cout<<"\n\n";

    return 0;
}