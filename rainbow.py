import board
import neopixel
from time import sleep

r = 0
g = 0
b = 0

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = .1

print("Make it red!")

while True:
    while r<255:
        r+=1
        dot.fill((r,g,b))

    while b>0:
        b-=1
        dot.fill((r,g,b))

    while g<255:
        g+=1
        dot.fill((r,g,b))

    while r>0:
        r-=1
        dot.fill((r,g,b))

    while b<255:
        b+=1
        dot.fill((r,g,b))

    while g>0:
        g-=1
        dot.fill((r,g,b))
    print("raimbow")
