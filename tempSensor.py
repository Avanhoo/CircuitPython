import board
from analogio import AnalogIn
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep

raw = AnalogIn(board.A2)
temp = 0
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)


while True:
    temp = map(raw, 0, 100, 0, 100)
    lcd.print("Temp: " + str(temp))
    if temp > 72:
        lcd.print("Too Hawt")
    elif temp < 68:
        lcd.print("Too Cold")
    else:
        lcd.print("Perfect")
    lcd.clear()