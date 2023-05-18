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