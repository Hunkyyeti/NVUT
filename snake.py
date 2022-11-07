#Too Do
# make a better start screen
# make a saved high score
def snake():
    import random
    import time
    import hw
    import keyboard
    blockSize = 6
    maxX = int(128/blockSize)
    maxY = int(64/blockSize)
    speed = 200
    inputRate = 4
    
    gameLoop = True
    while(gameLoop):
        score = 0
        direction = 3
        xCord = 2
        yCord = 2
        seedNum = 0
        snakeBody = [[2,1],[2,2]]
    
        
        
        snakeRunning = True
        
        while(hw.bA.value()):
            pass
        menuLoop = True
        while(menuLoop):
            hw.oled.fill(0)
            hw.oled.text("Snake",30, 10)
            hw.oled.text("Press A to Start",0, 30)
            hw.oled.text("Press Mod for",0, 40)
            hw.oled.text("menu",0, 50)
            hw.oled.show()
            menuInputLoop = True
            while(menuInputLoop):    
                if(hw.bA.value()):
                    menuInputLoop = False
                    menuLoop = False
                elif(hw.bMod.value()):
                    while(True):
                        menuChoice = hw.menu(["Block Size " + str(blockSize), "Speed " + str(speed),"Exit"])
                        if(menuChoice == 0):
                            blockSize = int(keyboard.keyboard(str(blockSize)))
                            maxX = int(128/blockSize)
                            maxY = int(64/blockSize)
                        elif(menuChoice == 1):
                            speed = int(keyboard.keyboard(str(speed)))
                        elif(menuChoice == 2):
                            menuInputLoop = False
                            break
                    
                         
                 
            seedNum += 100
            hw.utime.sleep_ms(1)

        random.seed(seedNum)
        fruitX = int(random.random() * maxX)
        fruitY = int(random.random() * maxY)

        while(snakeRunning):
            hw.oled.fill(0)
            #prints out snake
            for segment in snakeBody:
                x = segment[0]
                y = segment[1]
                topX = x * blockSize
                topY = y * blockSize
                bottomX = topX + blockSize
                bottomY = topY + blockSize
                hw.filledBox(topX,topY,bottomX,bottomY,1)
            if(True):
                topX = fruitX * blockSize
                topY = fruitY * blockSize
                bottomX = topX + blockSize
                bottomY = topY + blockSize
                hw.box(topX,topY,bottomX-1,bottomY-1,1)
            hw.oled.show()


            #Gets input, controls direction, waits (speed) ms
            inputLoop = speed
            while(inputLoop > 0):
                if(hw.bUp.value() and direction != 3):
                    direction = 1
                    break
                elif(hw.bRight.value() and direction != 4):
                    direction = 2
                    break
                elif(hw.bDown.value() and direction != 1):
                    direction = 3
                    break
                elif(hw.bLeft.value() and direction != 2):
                    direction = 4
                    break
                inputLoop -= inputRate
                hw.utime.sleep_ms(inputRate)
            hw.utime.sleep_ms(inputLoop)
            if(direction == 1):
                yCord -= 1
            elif(direction == 2):
                xCord += 1
            elif(direction == 3):
                yCord += 1
            elif(direction == 4):
                xCord -= 1

            #Ends game if snake leaves the bounds
            if(inputLoop > 0):
                hw.utime.sleep_ms(inputLoop)

            #ends game if snake hits itself
            if(xCord > maxX or xCord < 0 or yCord > maxY or yCord < 0):
                snakeRunning = False
            for segment in snakeBody:
                if(segment[0] == xCord and segment[1] == yCord):
                    snakeRunning = False

            if(fruitX == xCord and fruitY == yCord):
                score += 1
                newFruit = True
                while(newFruit):
                    seedNum = seedNum + 10000
                    random.seed(seedNum)
                    fruitX = int(random.random() * maxX)
                    seedNum = seedNum + 10000
                    random.seed(seedNum)
                    fruitY = int(random.random() * maxY)
                    print("fruity " + str(fruitX) + " " + str(fruitY))
                    newFruit = False
                    for segment in snakeBody:
                        if(segment[0] == fruitX and segment[1] == fruitY):
                            hw.utime.sleep_ms(1)
                            newFruit = True
            else:
                snakeBody.pop(0)
        
            snakeBody.append([xCord,yCord])

        hw.oled.fill(0)
        hw.oled.text("Score is " + str(score),20, 10)
        hw.oled.text("Press A to cont.",0, 30)
        hw.oled.text("Press B to end",0,40)
        hw.oled.show()
        while(hw.bA.value()):
            pass
        
        while(True):
            if(hw.bA.value()):
                break
            elif(hw.bB.value()):
                gameLoop = False
                break
            
snake()
