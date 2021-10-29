#Equipo 7
# Abiel Moisés Borja García     A01654937
# Alejandro Mariacca Santin     A01654102
# Con los puntos 1, 2, 3
#Equipo 7

from turtle import *
from random import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
cont = {'clicks': 0}
contNum = 0

taps = 0
counter_tiles = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    global mark, taps, counter_tiles
    "Update mark and hidden tiles based on tap."

    taps = taps + 1

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot

    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

        counter_tiles = counter_tiles + 2

    print(cont)
    cont['clicks'] +=1
    


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    if counter_tiles == 64:
        up()
        goto(-190, 165)
        color('white')
        write("Felicades, has acabado el juego", font = ('Arial', 10, 'normal') )
        goto(-190, 130)
        color('white')
        write("Has hecho {} taps".format(taps), font = ('Arial', 10, 'normal') )


    update()
    ontimer(draw, 100)    

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()