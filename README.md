# Cable of Tontents
- [Servo Work](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#servo-work)
- [Ultrasonic_Adventures](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#ultrasonic-adventures)
- [LCD_Shenanigans](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#lcd-shenanigans)
- [Motor Control](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#motor-control)

# Servo Work
Servo.py is a piece of code made to control a 180° servo. One button will spin the servo right, and the other left. 
Libraries required:
- [digitalio](https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html) 
- [servo](https://www.arduino.cc/reference/en/libraries/servo/)
- [simpleio](https://docs.circuitpython.org/projects/simpleio/en/latest/api.html)
- pwmio
- time
(you can assume the time library will be in almost every project)

## Video

![Servo Video](https://user-images.githubusercontent.com/113116247/193277068-8d9a1f83-d436-4896-8e4d-b3a8a932f824.gif)

## Code
<details>
<summary><b>Click to Show<b></summary>
    
<p>

```
    
    # Afton Van Hooser, servo control with buttons

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
</p>

</details>

## Reflection
I don't really know how any of the pwm outputs work, but this project has reminded me that circuitpython is inferior in every way to Arduino. Still, I now know how to do inputs & outputs. 

# Ultrasonic Adventures
Rainbow_dist.py uses an ultrasonic sensor to map distances from 5-35cm to a red, blue, green gradient.
Libraries required:
- adafruit_hcsr04
- neopixel
- simpleio

## Video

![Distance_Video](https://user-images.githubusercontent.com/113116247/193050734-0cc4c493-cea9-422a-865a-26fbb7094b95.gif)
    
## Code
<details>
<summary><b>Click to Show<b></summary>
    
<p>

```

    # Afton Van Hooser, neopixel color control based on distance sensor
    # SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
    # SPDX-License-Identifier: MIT

    import time
    import board
    import adafruit_hcsr04
    import neopixel
    import simpleio

    dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
    dot.brightness = .25
    sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
    d = 30
    r = 0
    g = 0
    b = 0
    while True:
        try:
            d = (sonar.distance)
            print (str(d) +" -   " + str(r) +", " + str(g) +", "+ str(b))
        except RuntimeError:
            print("Retrying!")
        time.sleep(0.05)


        r = simpleio.map_range(d,5, 17.5, 255, 0)

        b = simpleio.map_range(d,15, 20, 0, 255)
        if d >20 and d<25:
            b = simpleio.map_range(d,20, 25, 255, 0)
        if d<15 or d>25:
            b = 0
        g = simpleio.map_range(d,22.5, 35, 0, 255)

        if d<5:
            r=255
        if d>35:
            g=255
        dot.fill((r,g,b))\
```
</p>
    
</details>

## Reflection
It took me a long time to get the color gradients right because I kept confusing myself with the numbers. Thankfully the benevolent ultrasonic sensor decided to work with the library, so that part was painless. 

# LCD Shenanigans
Lcd.py is an lcd controller that uses inputs from capacitive touch. Needs touchio and a few custom lcd libraries for circuitpython.

## Video
    
![LCD Video](https://user-images.githubusercontent.com/113116247/193283964-bb62dbda-2795-4635-a4b6-926c1c3d4781.gif)

## Code
<details>
<summary><b>Click to Show<b></summary>
    
<p>

```  

    # Afton Van Hooser
    # touchio credit: https://learn.adafruit.com/circuitpython-essentials/circuitpython-cap-touch

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
```
</p>
    
</details>
 
## Reflection
I decided to go with capacitive touch instead of buttons for this one, which required the use of a 1 million Ω resistor. Don't know why, but the capacitive touch things are super duper sensitive, and if this resistor was unplugged at any point the whole thing crashed. As far as the lcd control went, it wasn't bad, but there were some pretty hilarious outputs when I forgot to clear the screen and it looped back onto itself.

# Motor Control
Control the power of a motor with a potentiometer.
    
## Video
    
![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/113116247/199739633-85a8cb55-a799-4342-ab2b-6019c33eb7c9.gif)

## Code 
<details>
<summary><b>Click to Show<b></summary>
    
<p>

```   

import time
import board
from analogio import AnalogIn
import pwmio
import simpleio

pot = AnalogIn(board.A2) # Sets up an input for the potentiometer
motor = pwmio.PWMOut(board.D7, duty_cycle=0, frequency=440, variable_frequency=True) # Sets up a PWM output for the motor
v = 0

while True:
    v = simpleio.map_range(pot.value, 2150, 65520, 0, 65535) # Maps the potentiometer ranges to those of the motor. The potentiometer never really reaches 0, so the min is set to 2150.
    print(int(v) / 65535) # Prints the potentiometer value from 0-1.
    time.sleep(.1)
    motor.duty_cycle = (int(v)) # Pushes the drive value to the motor    
```
</p>
    
</details>
    
## Reflection
It took me a long time to find PWM code that made enough sense to work. I still don't really get it, but the rest was easy.

# Next Assignment
    
## Video

## Code   
<details>
<summary><b>Click to Show<b></summary>
    
<p>
```
    
    
    
    ```
</p>  
    
</details>
    
## Reflection


