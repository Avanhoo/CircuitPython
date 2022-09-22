import board
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep

# get and i2c object
i2c = board.I2C()
touch = touchio.TouchIn(board.A4)
touch2 = touchio.TouchIn(board.A5)
count = 0
change = 1

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

print(touch.threshold)
while not touch.value and not touch2.value:
    lcd.print("Beans on Toast                  ")
    sleep(.75)
    lcd.print("Beans on Toast       (And Bolts)")
    sleep(.75)
while True:
    if touch.value:
        count += change
        lcd.clear()
        if change == 1:
            lcd.print("Counting Up     ")
        else:
            lcd.print("Counting Down   ")
        print(count)
        lcd.print(str(count))
        while touch.value:
            sleep(.05)

    if touch2.value:
        change = change*-1
        lcd.clear()
        if change == 1:
            lcd.print("Counting Up     ")
        else:
            lcd.print("Counting Down   ")
        lcd.print(str(count))
        print("switch!")
        while touch2.value:
            sleep(.1)
