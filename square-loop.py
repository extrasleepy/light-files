# CircuitPython demo - NeoPixel
import time
import board
import neopixel
import random
import digitalio
import adafruit_dotstar

pixel_pin = board.A1
num_pixels = 47
randnum = 0
grow = 0
decend = 0

builtin = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
builtin[0] = (0, 0, 2)

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.8, auto_write=False)

def color_chase(color, wait):
    grow = random.randint(0, 46)
    decend = grow
    print("grow point",grow)
    for i in range(grow,num_pixels):
        if decend > 0:
            decend -= 1
        pixels[i] = color
        pixels[decend] = color
        print("decend",decend,"i",i)
        time.sleep(wait)
        pixels.show()
    for decend in range(decend,0,-1):
        pixels[decend] = color
        print("decendcon",decend,"i",i)
        time.sleep(wait)
        pixels.show()
    time.sleep(900.0)

CYANNY = (120, 250, 100)
YELLOWYGREEN = (200, 250, 0)
SUPERWHITE = (180, 180, 180)
PURPLY = (250, 150, 180)
ORANGE = (250, 110, 40)
BLUISH = (150, 180, 200)
COLDDAY = (200, 130, 255)
NEWWHITE = (200, 250, 100)
BRIGHTYELLOWYGREEN = (200, 255, 30)

while True:
    randnum = random.randint(0, 8)
    print("color",randnum)
    if randnum == 0:
        color_chase(CYANNY, 0.1)  # Increase the num to slow down color
    if randnum == 1:
        color_chase(YELLOWYGREEN, 0.1)
    if randnum == 2:
        color_chase(SUPERWHITE, 0.1)
    if randnum == 3:
        color_chase(PURPLY, 0.1)
    if randnum == 4:
        color_chase(ORANGE, 0.1)
    if randnum == 5:
        color_chase(BLUISH, 0.1)
    if randnum == 6:
        color_chase(COLDDAY, 0.1)
    if randnum == 7:
        color_chase(NEWWHITE, 0.1)
    if randnum == 8:
        color_chase(BRIGHTYELLOWYGREEN, 0.1)