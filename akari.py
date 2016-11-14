################################################################################
#####                        Funciones del Tablero                         #####
################################################################################

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
        #buscar fila
        fil = i
        col = j
        while col < len(self.tablero):
            if self.tablero[i][col] == '*':
                return True
            elif self.tablero[i][col] != '-' and self.tablero[i][col] != '+':
                break
            col += 1
        col = j
        while col >= 0:
            if self.tablero[i][col] == '*':
                return True
            elif self.tablero[i][col] != '-' and self.tablero[i][col] != '+':
                break
            col -= 1
        #buscar columna
        while fil < len(self.tablero[0]):
            if self.tablero[fil][j] == '*':
                return True
            elif self.tablero[fil][j] != '-' and self.tablero[fil][j] != '+':
                break
            fil += 1
        fil = i
        while fil >= 0:
            if self.tablero[fil][j] == '*':
                return True
            elif self.tablero[fil][j] != '-' and self.tablero[fil][j] != '+':
                break
            fil -= 1
        return False

    def tablero_completo(self):
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
        if i > len(self.tablero) - 1 or j > len(self.tablero[0]) - 1:
            return False
        if i < 0 or j < 0:
            return False
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
        print("     ", end="")
        for x in range(len(self.tablero[0])):
            print(x, end=" ")
        print()
        print("    ", end="")
        for x in range(len(self.tablero[0])):
            print('=', end="=")
        print()
        for i in range(len(self.tablero)):
            if i < 10:
                print(" ", end="")
            print(i, '|', end=" ")
            for j in range(len(self.tablero[0])):
                print(self.tablero[i][j], end=" ")
            print()

    def tablero_resuelto(self):
        if self.tablero_completo() == False:
            return False
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                if self.tablero[i][j].isnumeric():
                    if self.luces(i, j) != int(self.tablero[i][j]):
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
        ## caso base ##
        if self.tablero_resuelto():
            return True
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                if self.esta_illuminada(i, j) == False and self.asignacion_valida(i, j) == True:
                    self.tablero[i][j] = '*'
                    ## llama recursiva ##
                    if self.resolver_tablero():
                        return True
                    else:
                        self.tablero[i][j] = '-'
        self.tablero = self.temptabs.pop()
        return False

################################################################################
#####                             Juego                                    #####
################################################################################

#def tablero_nuevo(arch):
#    if arch == "facil.txt":
#        archivo = open("facil.txt", 'w')
#        archivo.write("-,-,1,-,-,-,X\n")
#        archivo.write("-,-,-,-,-,-,-\n")
#        archivo.write("-,-,-,3,-,-,X\n")
#        archivo.write("-,-,X,X,3,-,-\n")
#        archivo.write("2,-,X,X,-,-,-\n")
#        archivo.write("-,-,-,-,-,-,-\n")
#        archivo.write("-,-,-,-,1,-,X")
#        archivo.close()
#    elif arch == "medio.txt":
#        archivo = open("medio.txt", 'w')
#        archivo.write("-,-,-,-,-,-,-,-,-,-\n")
#        archivo.write("-,4,-,-,X,-,-,-,2,-\n")
#        archivo.write("-,-,X,2,-,-,-,-,X,-\n")
#        archivo.write("-,-,-,-,X,0,-,-,X,-\n")
#        archivo.write("-,-,-,-,-,X,-,-,X,-\n")
#        archivo.write("-,-,-,-,-,-,-,-,-,-\n")
#        archivo.write("-,-,-,-,1,X,-,-,X,-\n")
#        archivo.write("-,1,-,-,-,-,-,0,X,-\n")
#        archivo.write("-,1,-,-,-,2,-,-,X,-\n")
#        archivo.write("-,-,-,-,-,-,-,-,-,-")
#        archivo.close()
#    elif arch == "dificil.txt":
#        archivo = open("dificil.txt", 'w')
#        archivo.write("1,-,-,-,-,-,X\n")
#        archivo.write("-,-,2,-,-,-,-\n")
#        archivo.write("-,-,-,-,-,2,-\n")
#        archivo.write("-,-,-,-,-,-,-\n")
#        archivo.write("-,3,-,-,-,-,-\n")
#        archivo.write("-,-,-,-,0,-,-\n")
#        archivo.write("0,-,-,-,-,-,X")
#        archivo.close()
#    elif arch == "bonus.txt":
#        archivo = open("bonus.txt", 'w')
#        archivo.write("-,-,-,-,0,-,-\n")
#        archivo.write("-,-,X,-,-,-,-\n")
#        archivo.write("1,-,-,X,-,2,-\n")
#        archivo.write("-,X,3,-,X,-,-\n")
#        archivo.write("-,3,-,X,-,-,1\n")
#        archivo.write("-,-,-,-,1,-,-\n")
#        archivo.write("-,-,0,-,-,-,-")
#        archivo.close()

print("***** Bienvenido a Akari *****")
print("Que quieres hacer?")
print("1. Jugar una nueva partida")
print("2. Jugar una partida guardada anteriormente")
hacer = input(">>> ")
print("Que dificultad quiere jugar?")
print("1. Facil")
print("2. Medio")
print("3. Dificil")
print("4. Bonus")
nivel = input(">>> ")
if hacer == '1':
    if nivel == '1':
        t = Tablero("facil.txt")
    if nivel == '2':
        t = Tablero("medio.txt")
    if nivel == '3':
        t = Tablero("dificil.txt")
    if nivel == '4':
        t = Tablero("bonus.txt")
if hacer == '2':
    if nivel == '1':
        t = Tablero("facil_g.txt")
    if nivel == '2':
        t = Tablero("medio_g.txt")
    if nivel == '3':
        t = Tablero("dificil_g.txt")
    if nivel == '4':
        t = Tablero("bonus_g.txt")

correctos = 0
incorrectos = 0
resuelto_auto = False
salido = False
while t.tablero_resuelto() == False:
    print()
    print('*******************************')
    t.print_tablero()
    print()
    print("Llevas", correctos, "intentos correctos y", incorrectos, "intentos incorrectos")
    print("Que quiere hacer?")
    print("1. Realizar jugada")
    print("2. Resolver tablero")
    print("3. Eliminar una ampolleta")
    print("4. Prender luces")
    print("5. Guardar partida actual")
    print("6. Salir del juego")
    ele = input(">>> ")
    if ele == '1':
        print("Donde quieres poner una ampolleta?")
        fil = int(input("Fila: "))
        col = int(input("Columna: "))
        if t.asignacion_valida(fil, col):
            t.tablero[fil][col] = '*'
            print("Asignacion valida!")
            correctos += 1
            continue
        else:
            print("Asignacion invalida.")
            incorrectos += 1
            continue
    if ele == '2':
        print("Resolviendo tablero...")
        resuelto_auto = True
        for i in range(len(t.tablero)):
            for j in range(len(t.tablero[0])):
                if t.tablero[i][j] == '*':
                    t.tablero[i][j] = '-'
        t.resolver_tablero()
        t.print_tablero()
        break
    if ele == '3':
        print("Que ampolleta quieres eliminar?")
        fil = int(input("Fila: "))
        col = int(input("Columna: "))
        if t.tablero[fil][col] == '*':
            t.tablero[fil][col] = '-'
            print("Ampolleta eliminada!")
            continue
        else:
            print("No hay ampolleta alli!")
    if ele == '4':
        for i in range(len(t.tablero)):
            for j in range(len(t.tablero[0])):
                if t.esta_illuminada(i, j) and t.tablero[i][j] == '-':
                    t.tablero[i][j] = '+'
        print()
        print("Tablero con luces prendidas:")
        t.print_tablero()
        for i in range(len(t.tablero)):
            for j in range(len(t.tablero[0])):
                if t.esta_illuminada(i, j) and t.tablero[i][j] == '+':
                    t.tablero[i][j] = '-'
    if ele == '5':
        if nivel == '1':
            archivo = open("facil_g.txt", 'w')
            for linea in t.tablero:
                tempstr = ','.join(linea)
                if t.tablero.index(linea) != len(t.tablero) - 1:
                    tempstr += '\n'
                archivo.write(tempstr)
            archivo.close()
        if nivel == '2':
            archivo = open("medio_g.txt", 'w')
            for linea in t.tablero:
                tempstr = ','.join(linea)
                if t.tablero.index(linea) != len(t.tablero) - 1:
                    tempstr += '\n'
                archivo.write(tempstr)
            archivo.close()
        if nivel == '3':
            archivo = open("dificil_g.txt", 'w')
            for linea in t.tablero:
                tempstr = ','.join(linea)
                if t.tablero.index(linea) != len(t.tablero) - 1:
                    tempstr += '\n'
                archivo.write(tempstr)
            archivo.close()
        if nivel == '4':
            archivo = open("bonus_g.txt", 'w')
            for linea in t.tablero:
                tempstr = ','.join(linea)
                if t.tablero.index(linea) != len(t.tablero) - 1:
                    tempstr += '\n'
                archivo.write(tempstr)
            archivo.close()
    if ele == '6':
        salido = True
        break

if resuelto_auto == False and salido == False:
    print("Felicitaciones! Completaste el tablero!")
    t.print_tablero()
   # if nivel == '1':
   #     tablero_nuevo("facil.txt")
   # if nivel == '2':
   #     tablero_nuevo("medio.txt")
   # if nivel == '3':
   #     tablero_nuevo("dificil.txt")
   # if nivel == '4':
   #     tablero_nuevo("bonus.txt")
