
"""
if __name__ == '__main__':
"""

def createPlayerSeloDict():

    filePath = "players.csv"
    isTrue = True

    while(isTrue):

        try:
            infile = open(filePath, "r")
            isTrue = False
        except:
            print("We couldn't find the player file")
            filePath = input("please enter the true player file path: ")

    header = infile.readline()
    playerSeloDict = {}

    for line in infile:

        lineList = line.strip().split(",")
        try:
            playerSeloDict[lineList[0]] = int(lineList[1])
        except ValueError:
            exit("Sorry the file includes a thing which is in wrong format. Program will be closed")

    infile.close()

    return playerSeloDict


def createGamesListOfDict():

    filePath = "games.csv"
    isTrue = True

    while(isTrue):

        try:
            infile = open(filePath, "r")
            isTrue = False
        except:
            print("We couldn't find the player file")
            filePath = input("please enter the true player file path: ")

    header = infile.readline()
    gamesListOfDict = []

    for line in infile:

        tempDict = {}
        lineList = line.strip().split(",")
        thirdElementList = lineList[2].split("-")

        tempDict[lineList[0]] = thirdElementList[0]
        tempDict[lineList[1]] = thirdElementList[1]

        gamesListOfDict.append(tempDict)

    infile.close()

    return gamesListOfDict



def fixThePlayerSeloDict():

    playerSeloDict = createPlayerSeloDict()
    gamesListOfDict = createGamesListOfDict()

    for game in gamesListOfDict:

        for key in game:

            if key not in playerSeloDict:
                playerSeloDict[key] = 1500

    return playerSeloDict, gamesListOfDict


# player_1 == winner, player_2 == loser
def delta(player_1, player_2):
    return 1 / (1 + 2**((player_1 - player_2) / 100))


def calculateTheResultSelo():

    fixedPlayerSeloDict, gamesListOfDict = fixThePlayerSeloDict()

    winnerName = ""
    loserName = ""
    for game in gamesListOfDict:
        for key in game:

            if game[key] == "1":
                winnerName = key
            else:
                loserName = key

        if("1/2" not in game.values()):

            changinPoint = int(200 * delta(fixedPlayerSeloDict[winnerName], fixedPlayerSeloDict[loserName]))

            seloDifference = abs(fixedPlayerSeloDict[winnerName] - fixedPlayerSeloDict[loserName])

            if(seloDifference < 500):
                fixedPlayerSeloDict[loserName] -= changinPoint

            fixedPlayerSeloDict[winnerName] += changinPoint

    return fixedPlayerSeloDict


print(f"Games --> {createGamesListOfDict()}")
print(f"PLayer and Selo Dictionary not fixed ---> {createPlayerSeloDict()}")

print(f"Name and Calculated Selo Dictionary ---> {calculateTheResultSelo()}")











