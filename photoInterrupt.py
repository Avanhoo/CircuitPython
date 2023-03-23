import board
from time import monotonic, sleep
from digitalio import DigitalInOut, Pull, Direction

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

now = monotonic()  # Time in seconds since power on
photo = DigitalInOut(board.D8)
photo.direction = Direction.INPUT
photo.pull = Pull.UP
count = 0
timeStart = 0

while True:
    if photo.value:
        count += 1
        while photo.value:
            pass
    if (float(timeStart + 4) < monotonic()):
        print("Interrupts: " + str(count))
        lcd.clear()
        lcd.print("Interrupts: " + str(count))
        count = 0
        timeStart = monotonic()