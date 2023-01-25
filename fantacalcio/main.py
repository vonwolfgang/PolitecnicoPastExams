


""" BUNU YAPAMADIM """

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

    for element in lineList:

        name, country, role, price = element.strip().split(",")

        if (role.lower()).strip() == "goalkeeper": goalKeepers[name] = int(price)
        if (role.lower()).strip() == "defender": defenders[name] = int(price)
        if (role.lower()).strip() == "midfielder": midfielders[name] = int(price)
        if (role.lower()).strip() == "forward": forwards[name] = int(price)

    return goalKeepers, defenders, midfielders, forwards


def buyPlayer():


    goalDict, defenderDict, midfielderDict, forwardDict = createRolDictionaries()

    goalBudget = 20
    defenderBudget = 40
    midfielderBudget = 80
    forwardBudget = 120

    goalTeamDict = {}
    defenderTeamDict = {}
    midfielderTeamDict = {}
    forwardTeamDict = {}

    decoyGoal = dict(goalDict)
    maxPrice = max(decoyGoal.values())
    for goal in


    print(f"Defender:  {defenderTeamDict}")
    print(f"Forw:  {forwardTeamDict}")
    print(f"Goal:  {goalTeamDict}")
    print(f"Mid:  {midfielderTeamDict}")









buyPlayer()


