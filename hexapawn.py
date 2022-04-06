from random import randint


def displayInDebbug(chessboard):
    for i in chessboard:
        print(i)

def playerDisplacement(chessboard, playerDisplacementList):
    good = False

    while good == False:
        pawn = int(input("pawn : "))
        displacement = int(input("displacement : "))
        
        for i in range(3):
            if pawn//10 == 1 and displacement >= -1 and displacement <= 1 and  pawn == playerDisplacementList[i][0][2] and displacement in playerDisplacementList[i]:
                line = playerDisplacementList[i][0][0]
                colon = playerDisplacementList[i][0][1]

                good = True
                break
            
        if good == False : print("\npawn or displacement is not valid\n")

    if displacement == 0:
        chessboard[line][colon] = 0
        chessboard[line-1][colon] = pawn
        return True
    
    elif displacement == -1:
        chessboard[line][colon] = 0
        chessboard[line-1][colon-1] = pawn
        return True
    
    elif displacement == 1:
        chessboard[line][colon] = 0
        chessboard[line-1][colon+1] = pawn
        return True

def botDisplacement(chessboard, botDisplacementList):
    r1 = randint(0, len(botDisplacementList)-1)
    r2 = randint(1, len(botDisplacementList[r1])-1)     

    line = botDisplacementList[r1][0][0]
    colon = botDisplacementList[r1][0][1]
    pawn = botDisplacementList[r1][0][2]
    displacement = botDisplacementList[r1][r2]

    if displacement == 0:
        chessboard[line+1][colon] = pawn

    elif displacement == -1:
        chessboard[line+1][colon-1] = pawn

    elif displacement == 1:
        chessboard[line+1][colon+1] = pawn

    chessboard[line][colon] = 0

    return[r1, r2]

def possibleBotDisplacement(chessboard):

    possibleDisplacementList = []

    for column in range(3): #listage des pions noirs qui peuvent se déplacés.
        for k in chessboard[column]:
            if k//10 == 2 :
                line = chessboard[column].index(k)

                local = []
                local.append([column, line, k])
 
                if column+1 < 3 :

                    if line-1 > -1 and chessboard[column+1][line-1]//10 == 1:
                        local.append(-1)

                    if chessboard[column+1][line]//10 == 0:
                        local.append(0)

                    if line+1 < 3 and chessboard[column+1][line+1]//10 == 1:
                        local.append(1)
                    
                    if len(local) != 1:
                        possibleDisplacementList.append(local)
                        
    return possibleDisplacementList

def possiblePlayerDisplacement(chessboard):

    possibleDisplacementList = []

    for column in range(3): #listage des pions noirs qui peuvent se déplacés.
        for k in chessboard[column]:
            if k//10 == 1 :
                line = chessboard[column].index(k)

                local = []
                local.append([column, line, k])
 
                if column-1 >= 0 :

                    if line-1 > -1 and chessboard[column-1][line-1]//10 == 2:
                        local.append(-1)

                    if chessboard[column-1][line]//10 == 0:
                        local.append(0)

                    if line+1 < 3 and chessboard[column-1][line+1]//10 == 2:
                        local.append(1)
                    
                    if len(local) != 1:
                        possibleDisplacementList.append(local)                    
    return possibleDisplacementList

def ai(botDisplacementList, blockedBotDisplacementList) :
    for i in blockedBotDisplacementList:
        if i[0] == botDisplacementList:
            r1 = i[1][0]
            r2 = i[1][1]

            del (botDisplacementList[r1]) [r2]

            if len(botDisplacementList[r1]) == 1 :
                del (botDisplacementList) [r1]

    return botDisplacementList

def playerVictoryTest(chessboard, botDisplacementList):
    if botDisplacementList == [] : return True
    
    for k in chessboard[0]:
        if k//10 == 1:
            return True
    
    return False

def botVictoryTest(chessboard, playerDisplacementList):
    if playerDisplacementList == [] : return True
    
    for k in chessboard[2]:
        if k//10 == 2:
            return True
    
    return False

blockedBotDisplacementList = []

playerScore = 0
botScore = 0

on = True
while on == True:
    
    chessboard = [
        [20, 21, 22],
        [0, 0, 0],
        [10, 11, 12]
    ]

    playerDisplacementList = [ 
        [[2,0, 10],0],
        [[2,1, 11],0],
        [[2,2, 12],0]
    ]
    botDisplacementList = []
    oldBotDisplacementList = []

    displayInDebbug(chessboard)

    gameEnd = False
    while gameEnd == False:

        playerDisplacement(chessboard, playerDisplacementList)

        oldBotDisplacementList = botDisplacementList

        botDisplacementList = possibleBotDisplacement(chessboard)
        playerWin = playerVictoryTest(chessboard, botDisplacementList)

        if playerWin == False:

            botDisplacementList = ai(botDisplacementList, blockedBotDisplacementList)

            botChoiceReturn = botDisplacement(chessboard, botDisplacementList)
            displayInDebbug(chessboard)
            
            playerDisplacementList = possiblePlayerDisplacement(chessboard)
            botWin = botVictoryTest(chessboard, playerDisplacementList)
            
        
        else :
            gameEnd = True
            playerScore+=1
            print("\nplayer win !\n")
            blockedBotDisplacementList.append([oldBotDisplacementList, botChoiceReturn])
        
        if botWin:
            gameEnd = True
            botScore+=1
            print("\nbot win !\n")