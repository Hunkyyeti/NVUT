import hw

def fileManager():
    fileManagerRunning = True
    currentDir = '/'

    #Contents of current Dir
    dirList = hw.os.listdir(currentDir)

    #the current file and it's string name
    topFile = 0
    topFileString = dirList[topFile]

    while(fileManagerRunning):
        hw.blk()
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
        while(inputLoop):
            #moves down
            if(hw.bDown.value() and topFile + 1 < len(dirList)):
                topFile += 1
                inputLoop = False
                print("down")
            #moves down
            elif(hw.bUp.value() and topFile > 0):
                topFile -= 1
                inputLoop = False
                print("up")
            #runs or opens file
            elif(hw.bA.value()):
                topFileLen = len(topFileString)
                #.py file handler
                if(topFileString[topFileLen - 2:topFileLen] == "py"):
                    print("file run")
                    hw.blk()
                    hw.execFile(topFileString)
                    inputLoop = False
                    fileManagerRunning = False
                #add another if statement here to handle more files
                else:
                    print("unknown file type")
                    hw.blk()
                    hw.oled.text("Can't open this",5,0)
                    hw.oled.text("file type Press",5,10)
                    hw.oled.text("A",5,20)
                    hw.oled.show()
                    while(not hw.bA.value()):
                        pass
                    inputLoop = False