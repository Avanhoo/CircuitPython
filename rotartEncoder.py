import board
from analogio import AnalogIn, AnalogOut
from digitalio import DigitalInOut, Direction
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep
import rotaryio

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
button = board(2)
rot = rotaryio.IncrementalEncoder(3, 4)
Rled = AnalogOut(8) #Setup for the 3 lights
Yled = AnalogOut(9)
Gled = AnalogOut(10)

Trafc = {1: 1, 2: 0, 3: 0}
spin = 1
lastSpin = 1
speed = 1


while True:
    spin = rot.position
    if spin > 3: # Keeps spin from 1-3
        spin = 1
    elif spin <1:
        spin = 3

    if spin != speed: # Turns on the highlighted light
        Trafc[spin] = .25

    if spin != lastSpin: # Updates the highlighted light
        print(spin)
        lcd.clear()
        lcd.print(spin)
        if lastSpin != speed: # Turns off the old highlighted light
           Trafc[lastSpin] = 0
        lastSpin = spin

    if button == True: # When the button is pressed it turns on the selected light and turns off the old one
        speed = spin
        Trafc[speed] = 0
        Trafc[spin] = 1
    
    Rled.value = Trafc[1]
    Yled.value = Trafc[2]
    Gled.value = Trafc[3]
