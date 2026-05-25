import matplotlib.pyplot as plt
import numpy as np

def graficar_recoleccion_vs_bateria(resultados):
    
    nombres_robots = list(resultados.keys()) # Obtención de nombres de los robots desde el diccionario
    
    basura_total = [resultados[robot]['basura_total'] for robot in nombres_robots] # Obtención de cantidad de basura recolectada 
    consumo_bateria = [resultados[robot]['consumo_bateria'] for robot in nombres_robots] #  Obtención de  de batería consumida 
    
    x = np.arange(len(nombres_robots)) # Definir cantidad de barras dependiendo del largo de la lista
    ancho = 0.35 # Definir ancho de cada barra
    
    plt.bar(x - ancho/2, basura_total, ancho, label='Basura Recolectada (kg)', color='green') # Desplazar barra de basura recolectada hacia la izquierda

    plt.bar(x + ancho/2, consumo_bateria, ancho, label='Batería Consumida (%)', color='red')  # Desplazar barra de batería consumida a la derecha
    
    plt.title('Rendimiento: Recolección vs Consumo Energético') # Título
    plt.ylabel('Cantidad') # Etiqueta eje y
    
    plt.xticks(x, nombres_robots) # definir el nombre de cada robot en el eje x
    
    plt.legend() # activar leyenda para los dos parámetros
    plt.grid(axis='y', linestyle='--', alpha=0.7) # ajustes de la cuadrícula horizontal
    
    plt.show() # crear gráfica
