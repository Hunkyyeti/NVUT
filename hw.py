#Hardware interface
import machine
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import math
import utime
import time
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
        
def line(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    length = 0
    if(math.fabs(dx) >= math.fabs(dy)):
        length = math.fabs(dx)
    else:
        length = math.fabs(dy)
    deltaX = dx / length
    deltaY = dy / length
    x = x1
    y = y1
    oled.pixel(int(x), int(y), color)
    i = 1
    while( i <= length ):
        x = x + deltaX;
        y = y + deltaY;
        oled.pixel(int(x), int(y), color)
        i+=1

    
        

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

def pressAToCont():
    while(bA.value()):
        pass
    while(not bA.value()):
        pass

def pressBToCont():
    while(bB.value()):
        pass
    while(not bB.value()):
        pass

        
def menu(items):
    mainLoop = True
    currentItem = 0
    upPressedTime = time.ticks_ms()
    downPressedTime = time.ticks_ms()
    inputWaitTime = 200
    while(mainLoop):
        oled.fill(0)
        i = 0
        firstFile = True
        while(i < 6 and i + currentItem < len(items)):
            if(firstFile):
                oled.text(">" + items[i + currentItem],5,i*10)
                firstFile = False
            else:
                oled.text(" " + items[i + currentItem],5,i*10)
            i += 1
        oled.show()
        inputLoop = True
        while(bA.value()):
            pass
        while(inputLoop):
                #moves down
                if(bDown.value() and currentItem + 1 < len(items) and (time.ticks_ms() - downPressedTime) > inputWaitTime):
                    downPressedTime = time.ticks_ms()
                    currentItem += 1
                    inputLoop = False
                #moves up
                elif(bUp.value() and currentItem > 0 and (time.ticks_ms()- upPressedTime) > inputWaitTime):
                    upPressedTime = time.ticks_ms()
                    currentItem -= 1
                    inputLoop = False
                elif(bA.value()):
                    return currentItem
