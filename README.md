# Cable of Tontents
- [Servo Work](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#Servo_Work)
- [Ultrasonic_Adventures](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#Ultrasonic_Adventures)
- [LCD_Shenanigans](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#LCD_Shenanigans)

# Servo_Work
Servo.py is a piece of code made to control a 180° servo. One button will spin the servo right, and the other left. 
Libraries required:
- [digitalio](https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html) 
- [servo](https://www.arduino.cc/reference/en/libraries/servo/)
- [simpleio](https://docs.circuitpython.org/projects/simpleio/en/latest/api.html)
- pwmio
- time
(you can assume the time library will be in almost every project)
## Code
```
#Afton Van Hooser, servo control with buttons

import board
from time import sleep
import pwmio
import servo
from digitalio import DigitalInOut, Direction
angle = 90


pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

button = DigitalInOut(board.D7) # Code from https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
button.direction = Direction.INPUT
button2 = DigitalInOut(board.D6)
button2.direction = Direction.INPUT


while True:
    if button.value and angle < 180:
        angle += 1

    if button2.value and angle > 0:
        angle -=1
    
    print(angle)
    my_servo.angle = angle
    sleep(0.01)
```

# Ultrasonic_Adventures
Rainbow_dist.py uses an ultrasonic sensor to map distances from 5-35cm to a red, blue, green gradient.
Libraries required:
- adafruit_hcsr04
- neopixel
- simpleio

## Code
```

```

# LCD_Shenanigans
Lcd.py is an lcd controller that uses inputs from capacitive touch. Needs touchio and a few custom lcd libraries for circuitpython.


```
git config --global user.name YOURUSERNAME
git config --global user.email YOURSCHOOLEMAIL
```
3. Return to step 3 of the previous section.
