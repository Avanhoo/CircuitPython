import time
import board
from analogio import AnalogIn
import pwmio
import simpleio

motor = pwmio.PWMOut(board.D11, duty_cycle=0, frequency=440, variable_frequency=True) # Sets up a PWM output for the motor


while True:
    for cycle in range(0, 65535, 15):  # Cycles through the full PWM range from 0 to 65535
        motor.duty_cycle = cycle  # Cycles the LED pin duty cycle through the range of values
        print(cycle)
    for cycle in range(65534, 0, -15):
        motor.duty_cycle = cycle
        print(cycle)