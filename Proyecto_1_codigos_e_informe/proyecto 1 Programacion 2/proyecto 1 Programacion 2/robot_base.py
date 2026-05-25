import math   # Librería matemática

class RobotBase:
    def __init__(self, nombre: str, capacidad_carga: float,
                 x_inicial: float = 0.0, y_inicial: float = 0.0, yaw_inicial: float = 0.0):

        # --- Atributos privados (encapsulación) ---
        self.__nombre = nombre                  # Nombre del robot
        self.__capacidad_carga = capacidad_carga # Capacidad máxima de basura (kg)
        self.__bateria = 100.0                  # Batería inicial
        self.__pos_x = x_inicial                # Posición inicial X
        self.__pos_y = y_inicial                # Posición inicial Y
        self.__yaw = yaw_inicial                # Orientación inicial en radianes
        self.__basura_recolectada = 0.0         # Basura acumulada
        self.__step_dt = 0.1                    # Intervalo de tiempo para muestreo

        # Atributos públicos (meta del robot)
        self.target_x = 5.0                     # Coordenada X de la meta
        self.target_y = 5.0                     # Coordenada Y de la meta

    #lectura de atributos privados
    def get_nombre(self): return self.__nombre
    def get_bateria(self): return self.__bateria
    def get_pos_x(self): return self.__pos_x
    def get_pos_y(self): return self.__pos_y
    def get_yaw(self): return self.__yaw
    def get_basura_recolectada(self): return self.__basura_recolectada

    #métodos protegidos (modifican estado interno)
    def _actualizar_pose(self, x, y, yaw):
        self.__pos_x, self.__pos_y, self.__yaw = x, y, yaw  # Actualiza posición y orientación

    def _reducir_bateria(self, cantidad):
        self.__bateria = max(0.0, self.__bateria - cantidad) # Reduce batería sin bajar de 0

    def _recolectar_basura(self, cantidad):
        espacio = self.__capacidad_carga - self.__basura_recolectada # Espacio disponible de almacenamiento
        self.__basura_recolectada += min(cantidad, espacio)          # Suma basura sin exceder capacidad

    # Métodos estáticos (calculos auxiliares)
    @staticmethod
    def calc_dist_to_goal(pos_x, pos_y, target_x, target_y):
        # Distancia euclidiana entre posición actual y meta
        # Esta sección se apoyó con IA, sino para confirmar la implementación más correcta y compacta
        #En los apuntes se menciona la fórmula, pero se busc ayuda externa para asegurar que el código en Python reflejara fielmente la teoría.
        return math.sqrt((target_x - pos_x)**2 + (target_y - pos_y)**2)

    

    @staticmethod
    def calc_yaw_error(pos_x, pos_y, yaw, target_x, target_y):
        # Calcula ángulo hacia la meta
        theta_meta = math.atan2(target_y - pos_y, target_x - pos_x)
        err = theta_meta - yaw
        # Normalización del error angular [-pi, pi] 
        # Esta sección se apoyó con IA porque en los laboratorios solo se menciona # la necesidad de normalizar, pero no se entrega la fórmula exacta.

        return (err + math.pi) % (2 * math.pi) - math.pi

    # Simulación cinemática
    def step(self, v, w):
        if self.__bateria <= 0:                 # Si batería agotada, robot se detiene
            return 0.0, True

        # Actualizar orientación (yaw)
        yaw_nuevo = self.__yaw + w * self.__step_dt
        yaw_nuevo = (yaw_nuevo + math.pi) % (2 * math.pi) - math.pi # Normalización

        # Actualizar posición (x, y)
        x_nuevo = self.__pos_x + v * math.cos(yaw_nuevo) * self.__step_dt
        y_nuevo = self.__pos_y + v * math.sin(yaw_nuevo) * self.__step_dt

        # Guardar nuevos valores
        self._actualizar_pose(x_nuevo, y_nuevo, yaw_nuevo)
    

        # Calcular distancia y error angular
        dist = RobotBase.calc_dist_to_goal(self.__pos_x, self.__pos_y, self.target_x, self.target_y)
        err_ang = RobotBase.calc_yaw_error(self.__pos_x, self.__pos_y, self.__yaw, self.target_x, self.target_y)

    
        reward = -dist - abs(err_ang)
        llegamos = False

        # Bonus si llega a la meta
        if dist < 0.5:
            reward += 100
            llegamos = True

        return reward, llegamos

    #Métodos abstractos para clases hijas
    def mover(self):
        raise NotImplementedError("Las clases hijas deben implementar mover().")

    def limpiar(self):
        raise NotImplementedError("Las clases hijas deben implementar limpiar().")
