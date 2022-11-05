#Hardware interface
import machine
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import math
import utime
import os
WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

# Explicit Method
sda=machine.Pin(4)
scl=machine.Pin(5)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
#  print(i2c.scan())
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)
#buttons
bLeft = Pin(6, Pin.IN, Pin.PULL_DOWN)
bUp = Pin(7, Pin.IN, Pin.PULL_DOWN)
bDown = Pin(8, Pin.IN, Pin.PULL_DOWN)
bRight = Pin(9, Pin.IN, Pin.PULL_DOWN)
bMod = Pin(11, Pin.IN, Pin.PULL_DOWN)
bA = Pin(12, Pin.IN, Pin.PULL_DOWN)
bB = Pin(10, Pin.IN, Pin.PULL_DOWN)
bStart = Pin(13, Pin.IN, Pin.PULL_DOWN)

def blk():
    oled.fill(0)
    oled.show()
    
def horiz(l,t,r,c):  # left, right , top
    n = r-l+1        # Horizontal line
    for i in range(n):
        oled.pixel(l + i, t, c)

def vert(l,t,b,c):   # left, top, bottom
    n = b-t+1        # Vertical line
    for i in range(n):
        oled.pixel(l, t+i,c)

def box(l,t,r,b,c):  # left, top, right, bottom
    horiz(l,t,r,c)   # Hollow rectangle
    horiz(l,b,r,c)
    vert(l,t,b,c)
    vert(r,t,b,c)

def filledBox(l,t,r,b,c):# left, top, right, bottom
    for i in range(t,b):
        m = r-l+1
        for j in range(l,r):
            oled.pixel(j, i, c)

def ring2(cx,cy,r,c):   # Centre (x,y), radius, colour
    for angle in range(0, 90, 2):  # 0 to 90 degrees in 2s
        y3=int(r*math.sin(math.radians(angle)))
        x3=int(r*math.cos(math.radians(angle)))
        oled.pixel(cx-x3,cy+y3,c)  # 4 quadrants
        oled.pixel(cx-x3,cy-y3,c)
        oled.pixel(cx+x3,cy+y3,c)
        oled.pixel(cx+x3,cy-y3,c)
