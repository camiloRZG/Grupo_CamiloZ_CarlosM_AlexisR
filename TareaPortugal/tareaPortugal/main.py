import pandas as pd
import os
from jugadores import Portero, Defensa, Mediocampista, Delantero

# Selección candidata al mundial
pais_elegido = 'Portugal'

# 11 jugadores titulares Nombre, Eedad, estatura_m, dorsal, estadística de posición en el campo
jugadores_titulares = [ 
    
    # 1 portero
    Portero('Diogo Costa', 26, 1.86, dorsal=22, atajadas_totales=115, partidos_invicto=25),
    
    # 4 defensas
    Defensa('Nuno Mendes', 23, 1.76, dorsal=19, balones_recuperados=72, tarjetas_rojas=0),
    Defensa('Ruben Dias', 29, 1.87, dorsal=4, balones_recuperados=140, tarjetas_rojas=4),
    Defensa('Gonçalo Inacio', 24, 1.85, dorsal=14, balones_recuperados=88, tarjetas_rojas=3),
    Defensa('Joao Cancelo', 32, 1.82, dorsal=2, balones_recuperados=95, tarjetas_rojas=5),
    
    # 4 mediocampistas
    Mediocampista('Joao Neves', 21, 1.74, dorsal=15, asistencias=14, tiros_libres=1),
    Mediocampista('Vitinha', 26, 1.72, dorsal=23, asistencias=32, tiros_libres=1),
    Mediocampista('Bruno Fernandes', 31, 1.79, dorsal=8, asistencias=90, tiros_libres=12),
    Mediocampista('Bernardo Silva', 31, 1.73, dorsal=10, asistencias=78, tiros_libres=1),
    
    # 2 delanteros
    Delantero('Cristiano Ronaldo', 41, 1.87, dorsal=7, goles_anotados=130, remates_al_arco=231),
    Delantero('Rafael Leao', 26, 1.88, dorsal=17, goles_anotados=38, remates_al_arco= 57)
]

print("--- SIMULADOR DE CAMPEON DEL MUNDO ---")

print("\nAcciones en la cancha:")

# Clase padre

print(jugadores_titulares[1].correr())           # Segundo jugador de la lista (Nuno Mendes, defensa) corre por la cancha
print(jugadores_titulares[4].pasar_balon())      # Quinto jugador de la lista (Joao Cancelo, defensa) le pasa el balón a un compañero
print(jugadores_titulares[8].celebrar_gol())     # Noveno jugador de la lista (Bernardo Silva, mediocampista) celebra el gol anotado

# Clase hija

# Portero
print(jugadores_titulares[0].despejar())         # Primer jugador de la lista (Diogo Costa, portero) despeja el balón
print(jugadores_titulares[0].atajar())           # Primer jugador de la lista (Diogo Costa, portero) ataja el balón

# Defensas
print(jugadores_titulares[3].marcar())           # Cuarto jugador de la lista (Gonçalo Inacio, defensa) marca al delantero rival
print(jugadores_titulares[2].recuperar())        # Tercer jugador de la lista (Ruben Dias, defensa) recupera el balón

# Mediocampistas
print(jugadores_titulares[6].dar_pase())         # Séptimo jugador de la lista (Vitinha, mediocampista) da un pase filtrado al espacio para el delantero
print(jugadores_titulares[5].presionar())         # Sexto jugador de la lista (Joao neves, mediocampista) presiona alto

# Delanteros
print(jugadores_titulares[9].patear_al_arco())   # Décimo jugador de la lista (Cristiano Ronaldo, delantero) patea al arco y mete gol
print(jugadores_titulares[10].regatear())  # Onceavo jugador de la lista (Rafael Leao, delantero) regatea y deja al defensa en el camino

print("\nRoles del equipo:") # Mostrar rol de los jugadores
for jugador in jugadores_titulares:
    print(f"{jugador.nombre} - {jugador.mostrar_rol()}")



# Lista vacía para almacenar datos
datos_jugadores = []

# Extraer atributos de los objetos a un diccionario
for jugador in jugadores_titulares:
    datos_jugadores.append({
        "Pais": pais_elegido,
        "Dorsal": jugador.dorsal,
        "Nombre": jugador.nombre,
        "Edad": jugador.edad,
        "Altura_m": jugador.altura,
        "Posicion": jugador.mostrar_rol() 
    })

# Convertir la lista a DataFrame de Pandas
dfequipo = pd.DataFrame(datos_jugadores)


print("Estadisticas de equipo (Pandas)")

# Imprimir tabla completa
print("\n1. La tabla completa del equipo:")
print(dfequipo.to_string())

# Calcular e imprimir promedio de edad
edad_promedio = dfequipo['Edad'].mean()
print(f"\n2. La edad promedio del equipo: {edad_promedio:.1f} años")

# Calcular e imprimir altura máxima
altura_max = dfequipo['Altura_m'].max()
print(f"\n3. La altura máxima del equipo: {altura_max} m")

# Contar e imprimir frecuencia de posiciones
print("\n4. La cantidad de jugadores por posición:")
print(dfequipo['Posicion'].value_counts().to_string())

# Agrupar por posición, promediar edades e imprimir
print("\n5. El promedio de edad por posición:")
print(dfequipo.groupby('Posicion')['Edad'].mean().to_string())

# Crear directorio 'Plantilla' si no existe
if not os.path.exists('output'):
    os.makedirs('output')

# Guardar DataFrame como archivo CSV
rutaarchivo = 'output/titulares_portugal.csv'
dfequipo.to_csv(rutaarchivo, index=False, encoding='utf-8')

print(f"Los datos fueron exportados correctamente a '{rutaarchivo}'.")
