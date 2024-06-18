freezing_pt = 32.0
scale_factor = 9.0 / 5.0

celsius = float(input("Ingrese la temperatura en Celsius: "))

fahrenheit = (celsius * scale_factor) + freezing_pt

print(f"La temperatura en Fahrenheit es {fahrenheit:.2f}")