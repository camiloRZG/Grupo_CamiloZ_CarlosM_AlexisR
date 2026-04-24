import numpy as np  

def calcular_movimiento(x, y, theta, v, omega, dt=0.1):
    # Limitar velocidad lineal entre -0.8 y 0.8
    v = np.clip(v, -0.8, 0.8)
    # Limitar velocidad angular entre -0.6 y 0.6
    omega = np.clip(omega, -0.6, 0.6)

    # Actualizar coordenada X
    x_nuevo = x + v * np.cos(theta) * dt
    # Actualizar coordenada Y
    y_nuevo = y + v * np.sin(theta) * dt
    # Actualizar orientación
    theta_nuevo = theta + omega * dt

    # Retorna la nueva posición
    return x_nuevo, y_nuevo, theta_nuevo


def distancia_al_objetivo(x, y, x_meta, y_meta):
    # Calcula la distancia entre la posición actual y la meta
    return np.sqrt((x_meta - x)**2 + (y_meta - y)**2)


def calcular_error_seguimiento(x_real, y_real, x_ideal, y_ideal):
    # Calcula el error entre la trayectoria real y la ideal
    errores = np.sqrt((x_real - x_ideal)**2 + (y_real - y_ideal)**2)
    return errores
