import board
from time import sleep
from analogio import AnalogIn

color = AnalogIn(board.A2)

sleep(1)
colorBase = color.value
pColor = 10000

for i in range(9):
    colorBase += color.value
    sleep(.05)
colorBase /= 10
print(colorBase)
while True:
    print("Base: " + str(colorBase))
    print("Sens: " + str(color.value))
    print("pErr: " + str((color.value - colorBase) / colorBase*100))
    sleep(.1)
""" if color.value < pColor:
        pColor = color
    if ((colorBase - int(color.value)) < 3000) or int(color.value) > colorBase:
        print("base")
    elif (int(color.value) - pColor) < 3000:
        print("mirror??")
    elif (int(color.value) < colorBase) and (int(color.value) > pColor):
        print("coppa?") """
    #Base:   3900
    #Copper: 2976
    #White:  3552
    #Grey:   3582