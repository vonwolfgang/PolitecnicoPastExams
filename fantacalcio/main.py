
def readFile():

    fileflag = True
    filePath = "fantafoot.txt"

    while(fileflag):

        try:
            infile = open(filePath, "r")
            lineList = infile.readlines()
            infile.close()
            fileflag = False
        except OSError:
            print("we coudln't find the file")
            filePath = input("enter again the file path: ")

    return lineList


def createRolDictionaries():

    lineList = readFile()

    goalKeepers = {}
    defenders = {}
    midfielders = {}
    forwards = {}

    goalBudget = 20 # 3 tane
    defenderBudget = 40 # 8 tane
    midfielderBudget = 80 # 8 tane
    forwardBudget = 120 # 6 tane

    for element in lineList:

        name, country, role, price = element.strip().split(",")

        if ((role.lower()).strip() == "goalkeeper" and int(price) < goalBudget): goalKeepers[name] = int(price)
        if ((role.lower()).strip() == "defender" and int(price) < defenderBudget): defenders[name] = int(price)
        if ((role.lower()).strip() == "midfielder" and int(price) < midfielderBudget): midfielders[name] = int(price)
        if ((role.lower()).strip() == "forward" and int(price) < forwardBudget): forwards[name] = int(price)

    return goalKeepers, defenders, midfielders, forwards


def sortDictDescending(dictionary):

    keyList = [key for key in dictionary]
    valueList = [dictionary[key] for key in dictionary]

    for index in range(len(valueList)):
        for index2 in range(len(valueList)):

            if(valueList[index] > valueList[index2]):

                valueList[index], valueList[index2] = valueList[index2], valueList[index]
                keyList[index], keyList[index2] = keyList[index2], keyList[index]

    sortedDict = {}
    for index in range(len(keyList)):
        sortedDict[keyList[index]] = valueList[index]

    return sortedDict

def buyPlay(budget, numOfPlayer, playerDict):

    boughtDict = {}

    nameList = [key for key in playerDict]
    valueList = [playerDict[key] for key in playerDict]

    for k in range(numOfPlayer):

        for index, key in enumerate(valueList):

            if(budget - valueList[index] >= numOfPlayer and valueList[index] < budget):

                boughtDict[nameList[index]] = valueList[index]
                budget -= valueList[index]
                nameList.remove(nameList[index])
                valueList.remove(valueList[index])
                numOfPlayer -= 1

            else:
                nameList.remove(nameList[index])
                valueList.remove(valueList[index])

    return boughtDict


def printAll():


    goalDict, defenderDict, midfielderDict, forwardDict = createRolDictionaries()
    sortedGoalDict, sortedDefenderDict, sortedMidDict, sortedForwDict = sortDictDescending(goalDict), sortDictDescending(defenderDict), sortDictDescending(midfielderDict), sortDictDescending(forwardDict)

    goalBudget = 20 # 3 tane
    defenderBudget = 40 # 8 tane
    midfielderBudget = 80 # 8 tane
    forwardBudget = 120 # 6 tane

    goalTeamDict = buyPlay(goalBudget, 3, sortedGoalDict)
    defendTeamDict = buyPlay(defenderBudget, 8, sortedDefenderDict)
    midTeamDict = buyPlay(midfielderBudget, 8, sortedMidDict)
    forwTeamDict = buyPlay(forwardBudget, 6, sortedForwDict)

    print("Goal keepers: ", end="")
    for key in goalTeamDict: print(f"{key} {goalTeamDict[key]}", end=" ")

    print("\n")
    print("Defenders: ", end="")
    for key in defendTeamDict: print(f"{key} {defendTeamDict[key]}", end=" ")

    print("\n")
    print("Midfielders: ", end="")
    for key in midTeamDict: print(f"{key} {midTeamDict[key]}", end=" ")

    print("\n")
    print("Forwarders: ", end="")
    for key in forwTeamDict: print(f"{key} {forwTeamDict[key]}", end=" ")


def main():
    printAll()

if __name__ == "__main__":
    main()

