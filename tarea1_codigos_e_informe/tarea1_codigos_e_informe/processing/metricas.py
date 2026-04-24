import numpy as np

def calcular_IAE(errores, dt):
    # Calcula error absoluto integrado
    return float(np.sum(np.abs(errores)) * dt)

def calcular_ISE(errores, dt):
    # Calcula error cuadrático integrado
    return float(np.sum(np.square(errores)) * dt)

def calcular_ITAE(errores, dt):
    # Calcula error absoluto ponderado por tiempo
    t = np.arange(len(errores)) * dt
    return float(np.sum(t * np.abs(errores)) * dt)

def calcular_ITSE(errores, dt):
    # Calcula error cuadrático ponderado por tiempo
    t = np.arange(len(errores)) * dt
    return float(np.sum(t * np.square(errores)) * dt)

def calcular_todas_las_metricas(errores, dt):
    # Calcula y redondea todas las métricas anteriores
    metricas = {
        "ISE": calcular_ISE(errores, dt),
        "IAE": calcular_IAE(errores, dt),
        "ITSE": calcular_ITSE(errores, dt),
        "ITAE": calcular_ITAE(errores, dt)
    }
    return {k: round(v, 2) for k, v in metricas.items()}

def calcular_mejora(valor_ppo, valor_mask):
    # Retorna porcentaje de mejora
    return ((valor_ppo - valor_mask) / valor_ppo) * 100