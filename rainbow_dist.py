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
    dot.fill((r,g,b))
