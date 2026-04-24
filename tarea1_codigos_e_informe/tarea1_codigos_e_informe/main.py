# =============================================================================
# main.py - Tarea 1 Programación 2 (PUCV)
# Integración de Módulos de Robótica y IA: "Robot Limpiaplayas"
# =============================================================================
import sys
import os
import numpy as np

# 1. IMPORTACIÓN DE MÓDULOS 
from data.robot_data import cargar_experimentos, generar_trayectoria_ideal, simular_lidar
from processing.cinematicas import calcular_movimiento, calcular_error_seguimiento, distancia_al_objetivo
from processing.metricas import calcular_todas_las_metricas, calcular_mejora
from visualization.graficos import plot_metricas, plot_lidar, plot_trayectorias

def main():
    print("--- INICIANDO SISTEMA DE EVALUACIÓN: PLAYABOT 2026 ---")

    # --- PASO 1: Carga de Datos Estáticos  ---
    # Cargamos el diccionario de diccionarios con los datos del paper
    datos_paper = cargar_experimentos()
    
    # --- PASO 2: Validación Cinemática ---
    print("\n[VALIDACIÓN] Verificando modelo físico del robot...")
    x_test, y_test, th_test = 0.0, 0.0, 0.0
    v_test, w_test = 0.5, 0.1  # Velocidades de prueba
    
    # Probamos el movimiento unitario
    x_n, y_n, th_n = calcular_movimiento(x_test, y_test, th_test, v_test, w_test)
    # Verificamos qué tan lejos quedó de una meta arbitraria (1,1)
    dist_test = distancia_al_objetivo(x_n, y_n, x_meta=1.0, y_meta=1.0)
    
    print(f" > Pose inicial: (0,0,0) -> Nueva Pose: ({x_n:.2f}, {y_n:.2f}, {th_n:.2f} rad)")
    print(f" > Distancia restante al objetivo (1,1): {dist_test:.2f}m")

    # --- PASO 3: Simulación de Sensor LiDAR  ---
    print("\n[SENSOR] Generando lectura de 36 sectores...")
    angulos, dist_reales, dist_norm = simular_lidar(n_sectores=36)
    plot_lidar(angulos, dist_reales, dist_norm)

    # --- PASO 4: Evaluación de Trayectorias ---
    print("\n[NAVEGACIÓN] Evaluando seguimiento de rutas...")
    
    # A) RUTA TRIANGULAR
    ruta_tri = [[0, 0], [4, 0], [2, 4], [0, 0]]
    x_id_tri, y_id_tri = generar_trayectoria_ideal(ruta_tri)
    
    # Simulamos lo que el robot hizo (PPO-Mask es más preciso que PPO)
    x_ppo_tri = x_id_tri + np.random.normal(0, 0.12, len(x_id_tri))
    y_ppo_tri = y_id_tri + np.random.normal(0, 0.12, len(y_id_tri))
    x_mask_tri = x_id_tri + np.random.normal(0, 0.04, len(x_id_tri))
    y_mask_tri = y_id_tri + np.random.normal(0, 0.04, len(y_id_tri))

    plot_trayectorias(x_ppo_tri, y_ppo_tri, x_mask_tri, y_mask_tri, ruta_tri, "triangulo")

    # B) RUTA CUADRADA
    ruta_cuad = [[0, 0], [4, 0], [4, 4], [0, 4], [0, 0]]
    x_id_cuad, y_id_cuad = generar_trayectoria_ideal(ruta_cuad)
    
    x_ppo_cuad = x_id_cuad + np.random.normal(0, 0.15, len(x_id_cuad))
    y_ppo_cuad = y_id_cuad + np.random.normal(0, 0.15, len(y_id_cuad))
    x_mask_cuad = x_id_cuad + np.random.normal(0, 0.05, len(x_id_cuad))
    y_mask_cuad = y_id_cuad + np.random.normal(0, 0.05, len(y_id_cuad))

    plot_trayectorias(x_ppo_cuad, y_ppo_cuad, x_mask_cuad, y_mask_cuad, ruta_cuad, "cuadrado")

    # --- PASO 5: Análisis de Métricas  ---
    # Usamos la ruta cuadrada para calcular el error matemático real
    errores_cuad_ppo = calcular_error_seguimiento(x_ppo_cuad, y_ppo_cuad, x_id_cuad, y_id_cuad)
    res_cuad = calcular_todas_las_metricas(errores_cuad_ppo, dt=0.1)
    
    print(f"\n[MÉTRICAS] Resultados PPO en Ruta Cuadrada:")
    for metrica, valor in res_cuad.items():
        print(f" > {metrica}: {valor}")

    # --- PASO 6: Comparativa Final del Paper  ---
    # Graficamos los datos históricos de la Tabla 6
    plot_metricas(datos_paper, ambiente="Real", ruta="simple")
    
    print("\n--- PROCESO FINALIZADO ---")
    print("Revise la carpeta 'resultados_graficos' para ver los reportes visuales.")

if __name__ == "__main__":
    main()