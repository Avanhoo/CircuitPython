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