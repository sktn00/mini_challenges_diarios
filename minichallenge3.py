def contar_vocales(cadena):
    vocales_encontradas = []
    vocales = ["a", "e", "i", "o", "u"]
    for letra in cadena:
        if letra.lower() in vocales:
            vocales_encontradas.append(letra.lower())
    return vocales_encontradas

palabras = input("Ingrese una palabra para contar las vocales: ")
resultado = contar_vocales(palabras)
print(f"Cantidad de vocales: {len(resultado)}\nVocales encontradas: {resultado}")