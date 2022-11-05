import hw
import keyboard
import textEditor
import time

def fileManager():
    fileManagerRunning = True
    currentDir = '/'

    #Contents of current Dir
    dirList = hw.os.listdir(currentDir)

    #the current file and it's string name
    topFile = 0
    upPressedTime = time.ticks_ms()
    downPressedTime = time.ticks_ms()
    inputWaitTime = 200

    while(fileManagerRunning):
        hw.oled.fill(0)
        topFileString = dirList[topFile]
        firstFile = True
        i = 0
        #Prints out files
        while(i < 6 and i + topFile < len(dirList)):
            if(firstFile):
                hw.oled.text(">" + dirList[i + topFile],5,i*10)
                firstFile = False
            else:
                hw.oled.text(" " + dirList[i + topFile],5,i*10)
            i += 1
        hw.oled.show()
        
        inputLoop = True
        #Checks for input
        while(hw.bMod.value()):
            pass
        while(hw.bA.value()):
            pass
        while(inputLoop):
            #moves down
            if(hw.bDown.value() and topFile + 1 < len(dirList) and (time.ticks_ms() - downPressedTime) > inputWaitTime):
                print("AGhhh")
                downPressedTime = time.ticks_ms()
                topFile += 1
                inputLoop = False
            #moves up
            elif(hw.bUp.value() and topFile > 0 and (time.ticks_ms()- upPressedTime) > inputWaitTime):
                upPressedTime = time.ticks_ms()
                topFile -= 1
                inputLoop = False
            #Renames a file
            elif(hw.bMod.value()):
                newFileName = keyboard.keyboard(topFileString)
                hw.os.rename(topFileString,newFileName)
                hw.oled.fill(0)
                hw.oled.text("file renamed to",5,0)
                hw.oled.text("press a to cont.",5,0)
                hw.oled.text(newFileName,5,10)
                hw.oled.show()
                while(not hw.bA.value()):
                    pass
                inputLoop = False
                while(hw.bA.value()):
                    pass
           #runs or opens file    
            elif(hw.bA.value()):
                topFileLen = len(topFileString)
                hw.oled.fill(0)
                #.py file handler
                print(topFileString[-2:])
                print(topFileString)
                if(topFileString[-2:] == "py"):
                    hw.oled.fill(0)
                    exec(open(topFileString).read())
                    inputLoop = False
                    fileManagerRunning = False
                #.txt file handler
                elif(topFileString[-3:] == "txt"):
                    textEditor.textEditor(topFileString)
                #add another if statement here to handle more file types
                else:
                    hw.oled.fill(0)
                    hw.oled.text("Can't open this",5,0)
                    hw.oled.text("file type Press",5,10)
                    hw.oled.text("A",5,20)
                    hw.oled.show()
                    while(not hw.bA.value()):
                        pass
                    inputLoop = False
