import board
from analogio import AnalogIn
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep
from simpleio import map_range

raw = AnalogIn(board.A2)
temp = 0
tChange = 0
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)


while True:
    #temp = map_range(raw.value, 0, 100, 0, 100)
    temp = round((raw.value-500)/ 576,1)
    if tChange != temp:    
        lcd.clear()
        lcd.print("T: " + str(temp) +"C  " + str(round((temp * 1.8) + 32,1)) + "F ")
        if temp > 24:
            lcd.print("Too Hawt")
        elif temp < 22:
            lcd.print("Too Cold")
        else:
            lcd.print("Perfect")
        tChange = temp
        print(temp)
    sleep(.1)
    