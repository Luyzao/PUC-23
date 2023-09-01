#include <iostream>
#include <cmath>
using namespace std;

int main() {
    float a, b, c, x1, x2, d;

    cout << "Insira o valor de a b c: ";
    cin >> a >> b >> c;

    if (a == 0) {
        cout << "\n\n\n\tDivisao por zero!";
    } else {
        d = (b * b) - (4 * a * c);
        if (d >= 0) {
            x1 = (-b + sqrt(d)) / (2 * a);
            x2 = (-b - sqrt(d)) / (2 * a);

            cout << "\nA raiz x1: " << x1;
            cout << "\nA raiz x2: " << x2;
        } else {
            cout << "\n\n\n\tRaízes complexas!";
        }
    }

    return 0;
}
