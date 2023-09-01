#include <stdio.h>

int main() {
    int inicio, fim;
    printf("Digite o valor de início do intervalo: ");
    scanf("%d", &inicio);
    printf("Digite o valor de fim do intervalo: ");
    scanf("%d", &fim);

    int somatorio = 0;

    // Garantindo que o início seja par, se não for
    // incrementamos para o próximo número par
    if (inicio % 2 != 0) {
        inicio++;
    }

    for (int i = inicio; i <= fim; i += 2) {
        somatorio += i;
    }

    printf("A soma dos números pares dentro do intervalo [%d, %d] é: %d\n", inicio, fim, somatorio);

    return 0;
}
