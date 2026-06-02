class Jugador:
    def __init__(self, nombre, edad, altura, dorsal):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dorsal = dorsal

    def correr(self):
        return f"{self.nombre} está corriendo por la cancha."

    def mostrar_rol(self):
        return "Soy un jugador de fútbol que participará en el Mundial 2026."

    def pasar_balon(self):
        return f"{self.nombre} realiza un pase a un compañero."

    def celebrar_gol(self):
        return f"{self.nombre} celebra un gol con su equipo. Gritando ¡¡¡¡SIIUUUUH!!!!"


class Portero(Jugador):                                                                         # Creamos las clases para cada tipo de jugador(Portero, Defensa, Mediocampista y Delantero) y heredamos de la clase padre Jugador
    def __init__(self, nombre, edad, altura, dorsal, atajadas_totales, partidos_invicto):       # Se entregan los valores solicitados, ademas de atributos propios como atajadas_totales y partidos_invictos
        super().__init__(nombre, edad, altura, dorsal)
        self.atajadas_historicas = atajadas_totales
        self.partidos_invicto = partidos_invicto

    def atajar(self):                                                                           # Se crean los metodos propios para portero en este caso atajar, despejar y mostrar_rol que es para todo tipo de jugador (
                                                                                                # define si es portero, defensa, mediocampista o delantero) 
        return f"{self.nombre} ha atajado el balón."

    def despejar(self):
        return f"{self.nombre} despeja el balón."

    def mostrar_rol(self):
        return "Portero"


class Defensa(Jugador):                                                                         # Se repite el mismo proceso para los 4 tipos de jugadores, con sus atributos propios y metodos propios solicitados
    def __init__(self, nombre, edad, altura, dorsal, balones_recuperados, tarjetas_rojas):
        super().__init__(nombre, edad, altura, dorsal)
        self.balones_recuperados = balones_recuperados
        self.tarjetas_rojas = tarjetas_rojas

    def marcar(self):
        return f"{self.nombre} marca al delantero rival."

    def recuperar(self):
        return f"{self.nombre} recupera el balón."

    def mostrar_rol(self):
        return "Defensa"


class Mediocampista(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, asistencias, tiros_libres):
        super().__init__(nombre, edad, altura, dorsal)
        self.asistencias = asistencias
        self.tiros_libres = tiros_libres

    def dar_pase(self):
        return f"{self.nombre} da un pase filtrado al espacio para el delantero."

    def presionar(self):
        return f"{self.nombre} presiona alto."

    def mostrar_rol(self):
        return "Mediocampista"


class Delantero(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, goles_anotados, remates_al_arco):
        super().__init__(nombre, edad, altura, dorsal)
        self.goles_anotados = goles_anotados
        self.remates_al_arco = remates_al_arco

    def patear_al_arco(self):
        return f"{self.nombre} patea con fuerza al arco y mete gol."

    def regatear(self):
        return f"{self.nombre} regatea y deja al defensa en el camino."

    def mostrar_rol(self):
        return "Delantero"