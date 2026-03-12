import turtle

puntas = int(input("Introduce el número de puntas de la estrella: "))

pantalla = turtle.Screen()
pantalla.title("Estrella con Turtle")

t = turtle.Turtle()

angulo = 180 - (180 / puntas)

for i in range(puntas):
    t.forward(200)
    t.right(angulo)

turtle.done()