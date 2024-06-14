numeros = str(input("Escriba una lista de numeros separados en ,:"))

lista_numeros = numeros.split(",")
lista_numeros.sort()

print(f"La lista de numeros ordenada de manera ascendente es {lista_numeros}")