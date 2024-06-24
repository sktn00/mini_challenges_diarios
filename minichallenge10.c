#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define LONGITUD 100

int es_palindromo(char *str);

int main() {
    char input[LONGITUD];
    
    printf("Ingrese una cadena de caracteres: ");
    fgets(input, sizeof(input), stdin);
    
    input[strcspn(input, "\n")] = 0;
    
    if (es_palindromo(input)) {
        printf("La cadena es un palindromo.\n");
    } else {
        printf("La cadena no es un palindromo.\n");
    }
    
    return 0;
}

int es_palindromo(char *str) {
    int left = 0;
    int right = strlen(str) - 1;
    
    while (left < right) {
        // Saltar caracteres no alfanumericos de la izquierda
        while (left < right && !isalnum(str[left])) {
            left++;
        }
        
        // Saltar caracteres no alfanumericos de la derecha
        while (left < right && !isalnum(str[right])) {
            right--;
        }
        
        // Comparar caracteres
        if (tolower(str[left]) != tolower(str[right])) {
            return 0; // No es un palindromo
        }
        
        left++;
        right--;
    }
    
    return 1; // Si es un palindromo
}