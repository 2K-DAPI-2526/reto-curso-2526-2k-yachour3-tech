# TABLERO INICIAL

tablero = [
["♜","♞","♝","♛","♚","♝","♞","♜"],
["♟","♟","♟","♟","♟","♟","♟","♟"],
[" "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "],
["♙","♙","♙","♙","♙","♙","♙","♙"],
["♖","♘","♗","♕","♔","♗","♘","♖"]
]


# FUNCION PARA GUARDAR TABLERO
def guardar_tablero(tablero, nombre):

    f = open(nombre, "a", encoding="utf-8")

    for fila in tablero:
        linea = ""
        for pieza in fila:
            linea += pieza + "\t"
        f.write(linea + "\n")

    f.write("\n")
    f.close()


# FUNCION PARA MOSTRAR TABLERO
def mostrar_tablero(tablero):

    for fila in tablero:
        print("\t".join(fila))


# PROGRAMA PRINCIPAL

nombre = input("Nombre del fichero: ")

guardar_tablero(tablero, nombre)

while True:

    print("\n1 - Hacer movimiento")
    print("2 - Terminar partida")
    print("3 - Ver tablero de un movimiento")

    opcion = input("Elige una opción: ")

    if opcion == "1":

        fila1 = int(input("Fila de la pieza: "))
        col1 = int(input("Columna de la pieza: "))

        fila2 = int(input("Fila destino: "))
        col2 = int(input("Columna destino: "))

        pieza = tablero[fila1][col1]
        tablero[fila1][col1] = " "
        tablero[fila2][col2] = pieza

        guardar_tablero(tablero, nombre)

        print("\nTablero actual:")
        mostrar_tablero(tablero)

    elif opcion == "2":
        print("Partida terminada")
        break

    elif opcion == "3":

        f = open(nombre, "r", encoding="utf-8")
        contenido = f.read()
        f.close()

        tableros = contenido.split("\n\n")

        mov = int(input("Número de movimiento: "))

        if mov < len(tableros):
            filas = tableros[mov].split("\n")
            for fila in filas:
                print(fila)

        else:
            print("Movimiento no existe")