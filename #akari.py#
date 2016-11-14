from copy import deepcopy

class Tablero:

    def __init__(self, nombre):
        self.tablero = []
        self.temptabs = []
        archivo = open(nombre, "r")
        for linea in archivo:
            row = []
            linea = linea.strip()
            linea = linea.split(',')
            for elem in linea:
                row.append(elem)
            self.tablero.append(row)

    def esta_illuminada(self, i, j):
        celda = self.tablero[i][j]
        if celda == '*':
            return True
        if celda != '-':
            return True
        #buscar columna
        fil = i
        col = j
        while col < len(self.tablero):
            if self.tablero[i][col] == '*':
                return True
            elif self.tablero[i][col] != '-':
                break
            col += 1
        col = j
        while col >= 0:
            if self.tablero[i][col] == '*':
                return True
            elif self.tablero[i][col] != '-':
                break
            col -= 1
        #buscar fila
        while fil < len(self.tablero[0]):
            if self.tablero[fil][j] == '*':
                return True
            elif self.tablero[fil][j] != '-':
                break
            fil += 1
        fil = i
        while fil >= 0:
            if self.tablero[fil][j] == '*':
                return True
            elif self.tablero[fil][j] != '-':
                break
            fil -= 1
        return False

    def esta_completo(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                if self.esta_illuminada(i, j) == False:
                    return False
        return True

    def luces(self, i, j):
        celda = self.tablero[i][j]
        num = 0
        if celda.isnumeric():
            if i > 0:
                if self.tablero[i - 1][j] == '*':
                    num += 1
            if i < len(self.tablero) - 1:
                if self.tablero[i + 1][j] == '*':
                    num += 1
            if j > 0:
                if self.tablero[i][j - 1] == '*':
                    num += 1
            if j < len(self.tablero[0]) - 1:
                if self.tablero[i][j + 1] == '*':
                    num += 1
        return num

    def junto_a_numero(self, i, j):
        resultos = []
        if i > 0:
            if self.tablero[i - 1][j].isnumeric():
                coord = [i - 1, j]
                resultos.append(coord)
        if i < len(self.tablero) - 1:
            if self.tablero[i + 1][j].isnumeric():
                coord = [i + 1, j]
                resultos.append(coord)
        if j > 0:
            if self.tablero[i][j - 1].isnumeric():
                coord = [i, j - 1]
                resultos.append(coord)
        if j < len(self.tablero[0]) - 1:
            if self.tablero[i][j + 1].isnumeric():
                coord = [i, j + 1]
                resultos.append(coord)
        return resultos

    def asignacion_valida(self, i, j):
        if self.tablero[i][j] != '-':
                return False
        if self.esta_illuminada(i, j) == False:
            for elem in self.junto_a_numero(i, j):
                f = elem[0]
                c = elem[1]
                if self.tablero[f][c].isnumeric():
                    if self.luces(f, c) >= int(self.tablero[f][c]):
                        return False
            return True
        return False

    def print_tablero(self):
        for fila in self.tablero:
            for elem in fila:
                print(elem, end=" ")
            print()

    def tablero_resuelto(self):
        if self.esta_completo() == False:
            return False
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                if self.tablero[i][j].isnumeric():
                    if self.luces(i, j) != int(self.tablero[i][j]):
                        return False
                if self.esta_illuminada(i, j) == False:
                    return False
        return True

    def disponibles(self, i, j):
        disp = []
        if i > 0:
            if self.tablero[i - 1][j] == '-' and self.esta_illuminada(i - 1, j) == False:
                coord = [i - 1, j]
                disp.append(coord)
        if i < len(self.tablero) - 1:
            if self.tablero[i + 1][j] == '-' and self.esta_illuminada(i + 1, j) == False:
                coord = [i + 1, j]
                disp.append(coord)
        if j > 0:
            if self.tablero[i][j - 1] == '-' and self.esta_illuminada(i, j - 1) == False:
                coord = [i, j - 1]
                disp.append(coord)
        if j < len(self.tablero[0]) - 1:
            if self.tablero[i][j + 1] == '-' and self.esta_illuminada(i, j + 1) == False:
                coord = [i, j + 1]
                disp.append(coord)
        return disp

    def ciertos(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                disp = self.disponibles(i, j)
                if self.tablero[i][j].isnumeric() and len(disp) != 0:
                    num = int(self.tablero[i][j])
                    if len(disp) <= num:
                        for elem in disp:
                            if self.asignacion_valida(elem[0], elem[1]) == True:
                                self.tablero[elem[0]][elem[1]] = '*'


    def num_luces(self):
        luces = 0
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                if self.tablero[i][j] == '*':
                    luces += 1
        return luces

    def resolver_tablero(self):
        temp = deepcopy(self.tablero)
        self.temptabs.append(temp)
        templuces = self.num_luces()
        self.ciertos()
        while self.num_luces() > templuces:
            templuces = self.num_luces()
            self.ciertos()
        if self.tablero_resuelto():
            return True
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                if self.esta_illuminada(i, j) == False and self.asignacion_valida(i, j) == True:
                    self.tablero[i][j] = '*'
                    if self.resolver_tablero():
                        return True
                    else:
                        self.tablero[i][j] = '-'
        self.tablero = self.temptabs.pop()
        return False


t = Tablero('bonus.txt')
t.print_tablero()
t.resolver_tablero()
print('-------------')
t.print_tablero()
