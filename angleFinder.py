
import board
from time import sleep
import pwmio
import servo

offset = -2

num = "90"
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.A5, duty_cycle=2 ** 15, frequency=50)

arm = servo.Servo(pwm)
spinny = servo.Servo(pwm2)
spinny.angle = 90 + offset
while True:
    spinny.angle = int(input("A: ")) + offset
    arm.angle = int(input("D: ")) - 10
