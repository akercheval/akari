class Tablero:

    def __init__(self, nombre):
        self.tablero = []
        archivo = open(nombre, "r")
        for linea in archivo:
            row = []
            linea.split(',')
            for elem in linea:
                row.append(elem)
            self.tablero.append(row)
