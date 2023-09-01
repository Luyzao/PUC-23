#include <iostream>
using namespace std;

int main() {
    int n;
    unsigned long long fatorial = 1; // Usando 'unsigned long long' para lidar com números grandes

    cout << "Insira um número inteiro não negativo: ";
    cin >> n;

    if (n < 0) {
        cout << "O número deve ser não negativo." << endl;
        return 1; // Encerrar o programa com erro
    }

    for (int i = 1; i <= n; i++) {
        fatorial *= i;
    }

    cout << "O fatorial de " << n << " é: " << fatorial << endl;

    return 0;
}
