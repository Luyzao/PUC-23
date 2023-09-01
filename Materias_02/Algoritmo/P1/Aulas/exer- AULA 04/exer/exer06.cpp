/*Exercício1: Construir um programa que faz a leitura de uma sequência de caracteres e contabiliza: quantas letras minúsculas foram digitadas,
quantas maiúsculas, quantos digitos e quantos de outros símbolos. Para a construção do algoritmo, deverá ser feita a leitura de um caractere
por vez, testar o que ele é, contabilizar e repetir esses passos N vezes. O valor de N também deve ser lido. Use o comando while para o
processo repetitivo. No final imprimir as 4 quantidades contabilizadas.*/

#include <iostream>
using namespace std;
int main()
{
    char C;
    int c_letraG,c_letraP, c_N, c_Outro,k,N;
    c_letraG=c_letraP=c_N=c_Outro=N=0;
    k=1;
    cout<<"\n\n Contador de caracter\n ";
    cout<<"-------------------------------\n";
    cout<<"Quantas caracteres deseja inserir?: ";cin>>N;

    while (k<=N)
    {
        /*Leitura Inicial*/
        cout<<"Insira a "<<k<<" caracter: ";cin>>C;

        /*Condicoes*/

        /*Verificar maiuscula - if(isupper(C))*/ 
        if (C>='A' && C<='Z')
            c_letraG+=1;

            /*Verificar minuscula - if(islower(C))*/
            else if (C>='a' && C<='z')
                c_letraP+=1;
                
            /*Verificar digito - if(isdigit(C))*/
            else if (C>='0'&& C<='9')
                c_N+=1;
            
            /*verificar outro caracter*/
            else
                c_Outro+=1;
            
            k+=1;

    }
        /* Impressão dos resultados */
    cout << "Quantidade de letras maiúsculas: " << c_letraG << endl;
    cout << "Quantidade de letras minúsculas: " << c_letraP << endl;
    cout << "Quantidade de dígitos: " << c_N << endl;
    cout << "Quantidade de outros símbolos: " << c_Outro << endl;
    return 0;
}