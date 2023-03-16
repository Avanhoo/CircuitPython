import board
from analogio import AnalogIn
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep
import rotaryio

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
button = board(2)
rot = rotaryio.IncrementalEncoder(3, 4)
spin = 0
lastSpin = 0
speed = 1

while True:
    spin = rot.position
    if spin > 3:
        spin = 1
    elif spin <1:
        spin = 3
    if spin != lastSpin:
        print(spin)
        lcd.clear()
        lcd.print(spin)
    lastSpin = spin
    if button == True:
        speed = spin
    if speed == 1:
        pass #red led
