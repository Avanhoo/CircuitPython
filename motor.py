import time
import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
import pwmio
import simpleio

pot = AnalogIn(board.A2)
motor = pwmio.PWMOut(board.D7, duty_cycle=0, frequency=440, variable_frequency=True)
v = 0

while True:
    v = simpleio.map_range(pot.value, 2150, 65520, 0, 65535)
    print(int(v) / 65535)
    time.sleep(.1)
    motor.duty_cycle = (int(v))