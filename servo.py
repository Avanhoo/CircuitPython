#Afton Van Hooser, servo control with buttons

import board
from time import sleep
import pwmio
import servo
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
import simpleio
angle = 0


pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
pot = AnalogIn(board.A2)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

button = DigitalInOut(board.D7) # Code from https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
button.direction = Direction.INPUT
button2 = DigitalInOut(board.D6)
button2.direction = Direction.INPUT


while True:
    angle = round(simpleio.map_range(pot.value, 2550, 65520, 0, 180))
    print(angle)
    if angle>90:
        for i in range(4,175):
            my_servo.angle = i
        for i in range (175,4,-1):
            my_servo.angle = i
    my_servo.angle = 90
    sleep(1)