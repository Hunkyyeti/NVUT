import hw
import time

def keyboard(finalString):
    hw.blk()
    text = [["`","1","2","3","4","5","6","7","8","9","0","-","="],[" ","q","w","e","r","t","y","u","i","o","p","[","]","\""],[" ","a","s","d","f","g","h","j","k","l",";","/'"],[" ","z","x","c","v","b","n","m",",",".","/"]]
    modText = [["~","!","@","#","$","%","^","&","*","(",")","_","+"],[" ","Q","W","E","R","T","Y","U","I","O","P","{","}","|"],[" ","A","S","D","F","G","H","J","K","L",":","\""],[" ","Z","X","C","V","B","N","M","<",">","?"]]
    keyX = 0
    keyY = 0
    modPressed = False
    upPressedTime = time.ticks_ms() + 10
    downPressedTime = time.ticks_ms() + 10
    leftPressedTime = time.ticks_ms() + 10
    rightPressedTime = time.ticks_ms() + 10
    inputWaitTime = 200

    keyboardRunning = True
    while(keyboardRunning):
        
        #Text being typed and keyboard text
        hw.oled.fill(0)
        hw.oled.text(">" + finalString[-14:],5,0)
        if(modPressed):
            hw.oled.text("~!@#$%^&*()_+",5,20)
            hw.oled.text(" QWERTYUIOP{}|",5,30)
            hw.oled.text(" ASDFGHJKL:\"",5,40)
            hw.oled.text(" ZXCVBNM<>?",5,50)
        else:
            hw.oled.text("`1234567890-=",5,20)
            hw.oled.text(" qwertyuiop[]\\",5,30)
            hw.oled.text(" asdfghjkl;'",5,40)
            hw.oled.text(" zxcvbnm,./",5,50)
        #Box around selected charecter
        #             X          Y              Width  Height color
        hw.oled.rect((keyX*8)+4,(keyY*10)+18,   10,    11,    1)
        hw.oled.show()
        
        hw.utime
        inputLoop = True
        while(inputLoop):
            while(hw.bA.value()):
                    pass
            while(hw.bB.value()):
                    pass
            while(hw.bMod.value()):
                    pass
            #Moves selected charecter
            if(hw.bUp.value() and keyY > 0 and (time.ticks_ms() - upPressedTime) > inputWaitTime):
                upPressedTime = time.ticks_ms()
                keyY -= 1
                inputLoop = False
            elif(hw.bDown.value() and keyY < 3 and (time.ticks_ms() - downPressedTime) > inputWaitTime):
                downPressedTime = time.ticks_ms()
                keyY += 1
                inputLoop = False
            elif(hw.bLeft.value() and keyX > 0 and (time.ticks_ms() - leftPressedTime) > inputWaitTime):
                leftPressedTime = time.ticks_ms()
                keyX -= 1
                inputLoop = False
            elif(hw.bRight.value() and keyX < 13 and (time.ticks_ms() - rightPressedTime) > inputWaitTime):
                rightPressedTime = time.ticks_ms()
                keyX += 1
                inputLoop = False
            #Types selected charecter
            elif(hw.bA.value()):
                if(modPressed):
                    finalString = finalString + modText[keyY][keyX]
                    inputLoop = False
                else:
                    finalString = finalString + text[keyY][keyX]
                    inputLoop = False
            #Delets last typed charecter
            elif(hw.bB.value()):
                finalString = finalString[:len(finalString)-1]
                inputLoop = False
            #Switches typing mode
            elif(hw.bMod.value()):
                modPressed = not modPressed
                inputLoop = False
            #Returns the string typed
            elif(hw.bStart.value()):
                inputLoop = False
                keyboardRunning = False
                if(finalString != str("")):
                    return finalString
                else:
                    return 
