import random
from robot_base import RobotBase

class RobotTresRuedas(RobotBase):                                                                   #RoboTresRueda Hereda de RobotBase
    def __init__(self, nombre, radio_rueda):                                                        #Constructor recibe nombre y radio_rueda
        super().__init__(nombre,capacidad_carga=20)                                                 #llamo al constructor padre, le paso nombre y la capacidad para RoboTresRuedas
        self.ruedas_calibradas = False                                                              #Atributo para RoboTresRuedas
        self.radio_rueda = radio_rueda                                                              #Guardo radio de rueda

    def  calibrar_giro(self):                                                                       #Inicio el Metodo Propio con self
        self.ruedas_calibradas = True                                                               #Cambio el atributo de ruedas calibradas a TRUE
        print(f"[{self.get_nombre()}]Calibrando ruedas de radio {self.radio_rueda} cm.")            #Printeo lo solicitado accediendo con get_nombre ya que es un archivo privado
              
    def mover(self):                                                                                #Metodo propio para moverse
        reward, finalizado = self.step(v=0.8,w=0.2)                                                 #Le doy los valores (v=0.8 w=0.2) al metodo step heredado para RoboTresRuedas
        return reward, finalizado                                                                   #El retorno solicitado de reward, finalizado
        
    def limpiar(self):                                                                              #Metodo propio para limpiar                                        #
        self._reducir_bateria(2.0)                                                                  #Llamo al metodo heredado _reducir_bateria y le asigno 2.0 para RoboTresRuedas                                                         
        basura = random.uniform(0.5,1.5)                                                            #Genera una cantidad aleatoria de basura entre esos rangos                                                        
        self._recolectar_basura(basura)                                                             #Llamo al metodo heredado _recolectar_basura y le entrego el valor aletorio de basura

class RobotOruga(RobotBase):                                                                        #Repito el mismo proceso para tension_oruga
    def __init__(self,nombre,tension_oruga):                                                        #...
        super().__init__(nombre,capacidad_carga=50)                                                 #Le entrego una capacidad_carga de 50 al constructor padre y el nombre
        self.tension_oruga = tension_oruga                                                          #Guardo la tension_oruga

    def ajustar_tension(self):                                                                      #Inicio el metodo propio ajustar_tension
        print(f"[{self.get_nombre()}] ajustando la tension de las orugas en {self.tension_oruga}.") #Printeo lo solicitado accediendo a nombre con get_nombre ya que es privado
    
    def mover(self):                                                                                #...
        reward, finalizado = self.step(v=0.3,w=0.8)                                                 #... ahora le entrego una v=0.3 y w=0.8 al metodo step heredado
        return reward, finalizado                                                                   #...

    def limpiar(self):                                                                              #...          
        self._reducir_bateria(4.5)                                                                  #...al metodo heredado le entrego el valor de 4.5
        basura = random.uniform(2,4)                                                                #... el rango de valores para basura ahora es entre 2 y 4     
        self._recolectar_basura(basura)

class RobotDron(RobotBase):                                                                         #Repito el mismo proceso para RobotDron
    def __init__(self, nombre, altura_maxima):                                                      #...
        super().__init__(nombre, capacidad_carga=5.0)                                               #... ahora le entrego una capacidad de carga 5.0 para RobotDron
        self.en_vuelo = False                                                                       #Nuevo atributo en_vuelo para RobotDron
        self.altura_maxima = altura_maxima                                                          #Guardo la altura máxima

    def despegar(self):                                                                             #...
        self.en_vuelo = True                                                                        #Cuando despega cambio el valor de en_vuelo a TRUE
        print(f"[{self.get_nombre()}] subiendo hasta {self.altura_maxima} metros de altura.")       #...
              
    def mover(self):                                                                                #...
        if self.en_vuelo:                                                                           #Si el RobotDron esta en vuelo entonces 
            reward, finalizado = self.step(v=2.5, w=1.0)                                            #llamo al metodo heredado step y le entrego v=2.5 w=1.0
            return reward, finalizado                                                               #Genero el valor de retorno solicitado
        else:                                                                                       #En cualquier otro caso
            return 0.0, False                                                                       #Retorna 0.0,False

    def limpiar(self):                                                                              #...
        if self.en_vuelo:                                                                           #Si el RobotDron esta en vuelo entonces
            self._reducir_bateria(3.0)                                                              #...le doy un valor de 3 a reducir bateria
            basura = random.uniform(0.1, 0.4)                                                       #...nuevo rango de 0.1 a 0.4
            self._recolectar_basura(basura)                                                         #...