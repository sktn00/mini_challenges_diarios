# Inversión de una Cadena: Escribe un programa que invierta una cadena de caracteres dada por el usuario

texto = str(input("Ingresa una cadena de caracteres: "))

for i in range(len(texto) - 1, -1, -1):
    print(texto[i], end="")