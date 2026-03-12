# MUROS DEL LABERINTO
muro = ((0,1),(0,2),(0,3),(0,4),
        (1,1),
        (2,1),(2,3),
        (3,3),
        (4,0),(4,1),(4,2),(4,3))

# CREAR LABERINTO VACIO
laberinto = []

for i in range(5):
    fila = []
    for j in range(5):
        fila.append(" ")
    laberinto.append(fila)

# COLOCAR MUROS
for m in muro:
    x, y = m
    laberinto[x][y] = "X"

# COLOCAR SALIDA
laberinto[4][4] = "S"

# MOSTRAR LABERINTO
print("Laberinto:")
for fila in laberinto:
    print(fila)


# LISTA DE MOVIMIENTOS
movimientos = []

# FUNCION PARA RESOLVER
def resolver(x, y):

    if laberinto[x][y] == "S":
        return True

    if laberinto[x][y] != " ":
        return False

    laberinto[x][y] = "V"

    if x+1 < 5:
        movimientos.append("Abajo")
        if resolver(x+1, y):
            return True
        movimientos.pop()

    if y+1 < 5:
        movimientos.append("Derecha")
        if resolver(x, y+1):
            return True
        movimientos.pop()

    if x-1 >= 0:
        movimientos.append("Arriba")
        if resolver(x-1, y):
            return True
        movimientos.pop()

    if y-1 >= 0:
        movimientos.append("Izquierda")
        if resolver(x, y-1):
            return True
        movimientos.pop()

    return False


# EJECUTAR BUSQUEDA
resolver(0,0)

print("\nCamino para salir del laberinto:")
print(movimientos)