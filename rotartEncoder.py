# Afton Van Hooser
# Rotary encoder traffic light menu
import board
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep
import rotaryio

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
sleep(1)
button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
rot = rotaryio.IncrementalEncoder(board.D3, board.D4, divisor=2) # Make sure the divisor is 2 so that it registers every increment
Rled = DigitalInOut(board.D8) #         Setup for the 3 lights
Rled.direction = Direction.OUTPUT
Yled = DigitalInOut(board.D9)
Yled.direction = Direction.OUTPUT
Gled = DigitalInOut(board.D10)
Gled.direction = Direction.OUTPUT

Trafc = {1: 1, 2: 0, 3: 0}
tName = {1: "Red", 2: "Yellow", 3: "Green"}
spin = 1
lastSpin = 1
speed = 1
last_pos = 0

lcd.print("Begin")
Trafc[1] = True
while True:
    spin += rot.position - last_pos
    last_pos = rot.position
    if spin > 3: # Keeps spin from 1-3
        spin = 1
    elif spin <1:
        spin = 3

    if spin != lastSpin: # Updates the highlighted light
        print(spin)
        lcd.clear()
        lcd.print("Change To:      "+ tName[spin]) # I use an array to avoid any if statement shenanigans
        lastSpin = spin

    if not button.value: # When the button is pressed it turns on the selected light and turns off the old one
        print("Press")
        Trafc[speed] = False # Turns off old light
        speed = spin # Updates speed value
        Trafc[spin] = True # Turns on new light
    
    Rled.value = Trafc[1]
    Yled.value = Trafc[2]
    Gled.value = Trafc[3]
    while not button.value: # Stops you from accidentally selecting another color when the button is pressed
        sleep(.1)
