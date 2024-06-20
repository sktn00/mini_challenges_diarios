# Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.

import string
import random

longitud = random.randint(8, 16)
caracteres = string.ascii_letters + string.digits + string.punctuation
contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
print(contrasena)