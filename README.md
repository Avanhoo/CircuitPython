# Cable of Tontents
- [Hello Circuitpython](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#hello-circuitpython)
- [Servo Work](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#servo-work)
- [Ultrasonic_Adventures](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#ultrasonic-adventures)
- [LCD_Shenanigans](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#lcd-shenanigans)
- [Motor Control](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#motor-control)
- [Temperature Sensor](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#temperature-sensor)
- [Rotary Encoder](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#rotary-encoder)
- [Photointerrupter](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#photointerrupter)
- [Onshape Certification](https://github.com/Avanhoo/CircuitPython/blob/master/README.md#onshape-certification)


# Hello Circuitpython
This was our first assignment with circuitpython (as opposed to arduino), and we wanted to control the onboard neopixel led.

## Proof
![ezgif com-resize](https://github.com/Avanhoo/CircuitPython/assets/113116247/9d797874-ac47-484a-b879-d740a6b21724)

## Code
<details>
<summary><b>Click to Show<b></summary>
    
<p>
    
```
import board
import neopixel
from time import sleep

r = 0
g = 0
b = 0

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = .25

print("Make it red!")

while True:
    r = int(input("How much red?"))
    g = int(input("How much green?"))
    b = int(input("How much blue?"))
    sleep(1)
    print("")
    dot.fill((r,g,b))
    
```
</p>  
    
</details>
    
## Reflection
I had used python before, so this wasn't too big of a shake-up for me, but it'll take some time to remember everything.

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



# Temperature Sensor
    I'm using a TMP36 temperature sensor to display temperature on a 2x16 lcd.
## Video

![ezgif com-video-to-gif (1)](https://user-images.githubusercontent.com/113116247/225033654-9b304b5f-3675-4836-9ecf-b80ef53a3a4d.gif)

## Code   
<details>
<summary><b>Click to Show<b></summary>
    
<p>
    
```

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
                       
```
</p>  
    
</details>
    
## Reflection

I had a very easy job making the lcd work as I already had code for it, though lcd's are often finicky. The temperature sensor gave a very large number as an output (10,000+), and though I found formulas to convert it to degrees, they didn't work, so I just found a random number to multiply it by that worked in giving me a degree reading. I'm not sure if this is accurate to be honest, as I believe the output scales with voltage, and I didn't do any fancy multiplication.


    
# Rotary Encoder
The goal here was to create a little traffic light system controlled by a rotary encoder. The encoder spin would be used to choose the light color you want, and the button to lock it in.
    
## Video
![ezgif com-optimize](https://user-images.githubusercontent.com/113116247/226633518-8a07b7b7-aa3c-4fb4-a822-e36892cf3d30.gif)

## Code   
<details>
<summary><b>Click to Show<b></summary>
    
<p>
    
```
    
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
```
</p>  
    
</details>
    
## Reflection
This code was very finicky. The rotary encoder I used needed a divisor of 2 instead of the default of 4 (thanks River), but you can change this value to adjust the "sensitivity" of the encoder. I had forgotten how to do all of my analog and digital inputs and outputs, so that's fun. Not much more to say. The rotary encoder library works very well, but the pins on the encoder are deceiving. You would think that 'CLK' is the button pin because it sounds like "click", but no, it's not, 'SW' is the button pin for some reason.



# Photointerrupter
We needed to do photinterrupters in circuitpython.
    
## Video
![ezgif com-optimize (1)](https://user-images.githubusercontent.com/113116247/227223146-cff0d73e-54dd-402c-bc37-3234e31b30ad.gif)

## Code   
<details>
<summary><b>Click to Show<b></summary>
    
<p>
    
```
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


```
</p>  
    
</details>    

## Reflection
This was very easy, just add 1 when pin.value and you're good.

# Onshape Certification
I feel like the preparation for the exam helped a lot and made me prepared. All of the things I had to model / assemble on the test were *very* similar to the practice documents.
    
![image](https://github.com/Avanhoo/Intermediate-CAD/assets/113116247/ecaded82-1bc0-4d47-81dd-beb629edf0fa)

    
    
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
