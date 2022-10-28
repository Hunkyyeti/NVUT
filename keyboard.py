import hw



def keyboard():
    hw.blk()
    text = [["`","1","2","3","4","5","6","7","8","9","0","-","="],[" ","q","w","e","r","t","y","u","i","o","p","[","]","\""],[" ","a","s","d","f","g","h","j","k","l",";","/'"],[" ","z","x","c","v","b","n","m",",",".","/"]]
    modText = [["~","!","@","#","$","%","^","&","*","(",")","_","+"],[" ","Q","W","E","R","T","Y","U","I","O","P","{","}","|"],[" ","A","S","D","F","G","H","J","K","L",":","\""],[" ","Z","X","C","V","B","N","M","<",">","?"]]
    keyX = 0
    keyY = 0
    finalString = ""
    modPressed = False

    keyboardRunning = True
    while(keyboardRunning):
        
        hw.blk()

        if(modPressed):
            hw.oled.text(">" + finalString,5,0)
            hw.oled.text("~!@#$%^&*()_+",5,20)
            hw.oled.text(" QWERTYUIOP{}|",5,30)
            hw.oled.text(" ASDFGHJKL:\"",5,40)
            hw.oled.text(" ZXCVBNM<>?",5,50)
        else:
            hw.oled.text(">" + finalString,5,0)
            hw.oled.text("`1234567890-=",5,20)
            hw.oled.text(" qwertyuiop[]\\",5,30)
            hw.oled.text(" asdfghjkl;'",5,40)
            hw.oled.text(" zxcvbnm,./",5,50)

        hw.oled.show()
        #hw.box(keyX*5,key)
        

        inputLoop = True
        while(inputLoop):
            if(hw.bUp.value() and keyY > 0):
                keyY -= 1
                inputLoop = False
            elif(hw.bDown.value() and keyY < 3):
                keyY += 1
                inputLoop = False
            elif(hw.bLeft.value() and keyX > 0):
                keyX -= 1
                inputLoop = False
            elif(hw.bRight.value() and keyX < 13):
                keyX += 1
                inputLoop = False
            elif(hw.bA.value()):
                if(modPressed):
                    finalString = finalString + modText[keyY][keyX]
                    inputLoop = False
                else:
                    finalString = finalString + text[keyY][keyX]
                    inputLoop = False
            elif(hw.bB.value()):
                finalString = finalString[:len(finalString)-1]
                inputLoop = False
            elif(hw.bMod.value()):
                modPressed = not modPressed
                inputLoop = False
            elif(hw.bStart.value()):
                inputLoop = False
                keyboardRunning = False
                return finalString

    print("keyboard")
    hw.utime.sleep(10)
    