# ==========================================
# main.py (Código del Profesor)
# ==========================================
from modelos_robot import RobotTresRuedas, RobotOruga, RobotDron
from robot_base import RobotBase
import analisis
import visualizacion
import math

def main():
    print("Iniciando despliegue de la flota de limpieza...\n")
    
    # Definimos la meta u objetivo al cual se deben dirigir los robots
    # Aquí es donde ocurre la simulación de ruta guiada
    x_goal = 5.0
    y_goal = 5.0
    
    # 1. POLIMORFISMO Y HERENCIA: Instanciación con atributos propios
    flota = [
        RobotTresRuedas("Triciclo-01", radio_rueda=15.0),
        RobotOruga("Tanque-Limpio", tension_oruga=85.0),
        RobotDron("Aero-Sweep", altura_maxima=20.0)
    ]
    
    # Asignamos explícitamente el objetivo a cada robot
    for robot in flota:
        robot.target_x = x_goal
        robot.target_y = y_goal
    
    # Demostración de métodos específicos (cada robot hace algo distinto antes de partir)
    print("--- Calibración Inicial ---")
    flota[0].calibrar_giro()
    flota[1].ajustar_tension()
    flota[2].despegar()
    print("---------------------------\n")

    historial_datos = []

    # 2. SIMULACIÓN: 20 pasos de limpieza
    for paso in range(1, 21):
        print(f"\n[ Paso de Simulación: {paso} ]")
        for robot in flota:
            # Cada robot usa su polimorfismo para mover y limpiar
            recompensa, llegamos = robot.mover()
            robot.limpiar() 
            
            # Extraemos la posición y orientación usando encapsulamiento (getters)
            # Notar que ahora utilizamos get_yaw() que estaba definido pero sin uso en la versión anterior
            pos_x = robot.get_pos_x()
            pos_y = robot.get_pos_y()
            yaw = robot.get_yaw()
            
            # USO DE MÉTODOS ESTÁTICOS: Monitoreamos la ruta utilizando los métodos de RobotBase
            # Esto evalúa la distancia restante al objetivo y el error de giro (desviación)
            distancia_restante = RobotBase.calc_dist_to_goal(pos_x, pos_y, x_goal, y_goal)
            error_giro = RobotBase.calc_yaw_error(pos_x, pos_y, yaw, x_goal, y_goal)
            
            # Lógica en la ruta: Si la distancia es menor a 2.5 metros, se realiza una acción especial
            # En este caso, simulamos que encuentran una "zona de alta suciedad" cerca de la meta
            if distancia_restante < 2.5 and not llegamos:
                print(f"  -> {robot.get_nombre()}: ¡Entrando a zona de aproximación! (Dist: {distancia_restante:.2f}m).")
                # Un pequeño aumento extra de basura recolectada al estar cerca de la meta
                # Nota: usamos el método protegido _recolectar_basura para mantener el encapsulamiento de la capacidad
                robot._recolectar_basura(0.2)
                
            # Si el robot presenta un error angular alto (mayor a 45 grados), advertimos sobre la desviación
            if abs(error_giro) > (math.pi / 4):
                 print(f"  -> {robot.get_nombre()}: Advertencia de desvío de ruta (Error angular: {error_giro:.2f} rad).")
            
            # 3. ENCAPSULAMIENTO: Uso estricto de getters para registrar el historial
            historial_datos.append([
                paso,
                robot.get_nombre(),
                pos_x,
                pos_y,
                robot.get_bateria(),
                robot.get_basura_recolectada()
            ])
            
            if llegamos:
                print(f"¡El robot {robot.get_nombre()} ha llegado a la meta en el paso {paso}!")

    print("\nTurno finalizado. Procesando datos de rendimiento...\n")

    # 4. ANÁLISIS (NumPy)
    resultados = analisis.comparar_rendimiento(historial_datos)
    
    print("--- Resultados de Eficiencia ---")
    for nombre, datos in resultados.items():
        print(f"Robot: {nombre}")
        print(f"  - Batería consumida: {datos['consumo_bateria']:.1f}%")
        print(f"  - Basura total: {datos['basura_total']:.1f} kg")
        print(f"  - Eficiencia (kg/%): {datos['eficiencia']:.2f}")

    # 5. VISUALIZACIÓN (Matplotlib)
    visualizacion.graficar_recoleccion_vs_bateria(resultados)

if __name__ == "__main__":
    main()