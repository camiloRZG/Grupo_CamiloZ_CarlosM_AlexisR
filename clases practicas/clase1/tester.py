print("Ingrese 1 para calcular resistencia en SERIE.")
print("Ingrese 2 para calcular resistencia en PARALELO.")

opcion = int(input("Opción: "))

# Solicitar el número de resistencias
num_resistencias = int(input("Ingrese el número de resistencias: "))


# Inicializar el cálculo de la resistencia equivalente
if opcion == 1:  # Cálculo en SERIE
    resistencia_equivalente = 0
elif opcion == 2:  # Cálculo en PARALELO
    resistencia_equivalente = 0  # Usaremos la suma de inversos

# Pedimos los valores de las resistencias y calculamos en el momento
for i in range(1, num_resistencias + 1):
    resistencia = float(input(f"Ingrese la resistencia {i} (Ω): "))
    # Cálculo inmediato
    if opcion == 1:  # Suma directa para SERIE
        resistencia_equivalente=resistencia+resistencia
    elif opcion == 2:  # Suma de inversos para PARALELO
        resistencia_equivalente += 1 / resistencia
# Cálculo final para paralelo (invertimos la suma de inversos)
if opcion == 2:
    resistencia_equivalente = 1 / resistencia_equivalente

# Mostrar el resultado final
if opcion == 1:
    print(f"\nLa resistencia equivalente en SERIE es: {resistencia_equivalente:.2f} Ω")
elif opcion == 2:
    print(f"\nLa resistencia equivalente en PARALELO es: {resistencia_equivalente:.2f} Ω")

if opcion == 1:
    print(f"\nLa resistencia equivalente en SERIE es: {resistencia_equivalente:.2f} Ω")
elif opcion == 2:
    print(f"\nLa resistencia equivalente en PARALELO es: {resistencia_equivalente:.2f} Ω")