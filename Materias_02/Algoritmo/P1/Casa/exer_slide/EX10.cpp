#include <iostream>
using namespace std;

/*verifica se caractere digitado é uma das vogais - se for, escrever se “minúscula” ou “maiúscula” se não for vogal, escrever mensagem: “outro caractere”*/



int main()

{
    char caracter;
    cout<<"\n\n Insira um caracter: ";cin>>caracter;

    switch (caracter) {
        case 'a': case 'e': case 'i': case 'o': case 'u': cout<< "Vogal Minuscula"; break;

        case 'A': case 'E': case 'I': case 'O': case 'U': default: cout<<"Outro caracter";

    } 

    cout<<"\n\n";

    return 0;
}