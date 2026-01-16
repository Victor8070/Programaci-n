
class equipo:
    def __init__(self, nom_eq):
        self.nombre_equipo = nom_eq


class jugador:
    #constructor
    def __init__(self, dor, nom, eq):
        self.dorsal = dor
        self.nombre = nom
        self.equipo = eq
    
    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre} : {self.equipo}")

#Programa Principal
equipo1 = equipo("FC Barcelona")
equipo2 = equipo("Juventus")

jugador1 = Jugador(10, "Messi", equipo1)
jugador2 = Jugador(7, "Cristiano", equipo2,)

jugador1.mostrar()
jugador2.mostrar()