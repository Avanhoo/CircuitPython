import board
from time import sleep
from analogio import AnalogIn

color = AnalogIn(board.A2)

sleep(1)
baseC = color.value
pColor = 10000

while True:
    print(color.value)
    sleep(.1)
""" if color.value < pColor:
        pColor = color
    if ((baseC - int(color.value)) < 3000) or int(color.value) > baseC:
        print("base")
    elif (int(color.value) - pColor) < 3000:
        print("mirror??")
    elif (int(color.value) < baseC) and (int(color.value) > pColor):
        print("coppa?") """
    #Base:   3900
    #Copper: 2976
    #White:  3552
    #Grey:   3582