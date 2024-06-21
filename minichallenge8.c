/* Escribir un programa que pida al usuario dos números y los sume */
#include <stdio.h>

int main() {
	int num1, num2;
	printf("Ingrese dos numeros separados por espacio para sumar: ");
	scanf("%d %d", &num1, &num2);

	printf("La suma es de %d\n", num1 + num2);

	return 0;
}