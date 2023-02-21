import board
from time import sleep
import pwmio
import servo
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
import simpleio

pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
pot = AnalogIn(board.A2)
angle = 0
Pangle = 0
send = 0

while True:
    Pangle = angle
    angle = simpleio.map_range(pot.value, 2550, 65520, 0, 180)
    angle = round(angle)
    send = angle
    if (abs(angle-Pangle)<2):
        send = round((angle + Pangle)/2)
    my_servo.angle = send
    print(send)
    sleep(.1)