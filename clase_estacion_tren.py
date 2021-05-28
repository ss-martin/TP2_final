# Grupo: 18
# Integrante: Carlos Montero Morales, Tomás Papantos, Martín Saavedra Sanchez

class EstacionDeTren:
    def __init__ (self, nombre, linea, ramal, lat, lng):
        self._nombre = nombre
        self._linea = linea
        self._ramal = ramal
        self._lat = float(lat)
        self._lng = float(lng)

    def __repr__ (self):
        return('('+self._linea + ';' + self._ramal + ';' + self._nombre+')')
    #metodo para calcular la distancia euclidia
    def distancia (self, lat, lng):
        distancia_euclidea = ( (self._lat - lat) ** 2 + ((self._lng) - lng) ** 2 ) ** 0.5
        return distancia_euclidea
    #metodo para comparar igualdad
    def __eq__ (self, other):
        return (self._nombre == other._nombre
            and self._linea == other._linea
            and self._ramal == other._ramal)
    #metodo para comparar menor extricto
    def __lt__ (self, other):
        if (self._linea < other._linea):
            return True
        elif (self._linea == other._linea and self._ramal < other._ramal):
            return True
        elif (self._linea == other._linea and self._ramal == other._ramal \
                and self._nombre < other._nombre):
            return True
        else:
            return False
    #metodo que devuelve nombre de estacion
    def nombre(self):
        return (self._nombre)
    #metodo que devuelve nombre linea
    def linea(self):
        return self._linea
    #metodo que devuelve nombre de ramal
    def ramal(self):
        return (self._ramal)
