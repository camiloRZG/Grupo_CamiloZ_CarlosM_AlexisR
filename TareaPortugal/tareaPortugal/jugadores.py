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


class Portero(Jugador):

    def __init__(self, nombre, edad, altura, dorsal, atajadas_totales, partidos_invicto):
        super().__init__(nombre, edad, altura, dorsal)
        self.atajadas_historicas = atajadas_totales     # Total de atajadas en su carrera
        self.partidos_invicto    = partidos_invicto     # Partidos sin recibir gol

    def atajar(self):
        return f"{self.nombre} Ha atajado el balón."

    def despejar(self):
        return f"{self.nombre} Despeja el balón."

    def mostrar_rol(self):
        return "Portero"


class Defensa(Jugador):

    def __init__(self, nombre, edad, altura, dorsal, balones_recuperados, tarjetas_rojas):
        super().__init__(nombre, edad, altura, dorsal)
        self.balones_recuperados = balones_recuperados  # Balones recuperados en su carrera
        self.tarjetas_rojas      = tarjetas_rojas       # Cantidad de Tarjetas Rojas en su carrera

    def marcar(self):
        return f"{self.nombre} Marca al delantero rival."

    def recuperar(self):
        return f"{self.nombre} Recupera el balón."

    def mostrar_rol(self):
        return "Defensa"


class Mediocampista(Jugador):

    def __init__(self, nombre, edad, altura, dorsal, asistencias, tiros_libres):
        super().__init__(nombre, edad, altura, dorsal)
        self.asistencias  = asistencias     # Asistencias de gol en su carrera
        self.tiros_libres  = tiros_libres   # Total de tiros libres 

    def dar_pase(self):
        return f"{self.nombre} Da un pase filtrado al espacio para el delantero."

    def presionar(self):
        return f"{self.nombre} Presiona alto."

    def mostrar_rol(self):
        return "Mediocampista"


class Delantero(Jugador):

    def __init__(self, nombre, edad, altura, dorsal, goles_anotados, remates_al_arco):
        super().__init__(nombre, edad, altura, dorsal)
        self.goles_anotados    = goles_anotados    # Goles marcados en su carrera
        self.remates_al_arco   = remates_al_arco   # Total de remates al arco

    def patear_al_arco(self):
        return f"{self.nombre} Patea con fuerza al arco y mete gol"

    def regatear(self):
        return f"{self.nombre} Regatea y deja al defensa en el camino."

    def mostrar_rol(self):
        return "Delantero"