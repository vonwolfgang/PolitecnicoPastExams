

def readFile():

    fileflag = True
    filePath = "scores.txt"
    while(fileflag):

        try:
            infile = open(filePath, "r")
            lineList = infile.readlines()
            infile.close()
            fileflag = False
        except OSError:
            print("We couldn't find the file")
            filePath = input("enter the file path again: ")

    return lineList

def createScoreDict():

    lineList = readFile()

    femalePlayerScoreDict = {}
    countryScoreDict = {}

    maxFemalScore = 0

    for line in lineList:

        tempList = line.strip().split(" ")

        fullName = f"{tempList[0]} {tempList[1]}"
        sex = tempList[2]
        nation = tempList[3]
        scoreList = tempList[4: ]

        scoreList = [float(x) for x in scoreList]
        scoreList.sort()

        countryScore = sum(scoreList[1: 4])

        if(nation in countryScoreDict):
            countryScoreDict[nation] += countryScore
        else:
            countryScoreDict[nation] = countryScore

        if(sex == "F"):

            currentFemalScore = scoreList[0] + scoreList[1] + scoreList[2]
            femalePlayerScoreDict[fullName] = [nation, currentFemalScore]
            if(currentFemalScore > maxFemalScore): maxFemalScore = currentFemalScore

    return maxFemalScore, femalePlayerScoreDict, countryScoreDict

def printAll():

    maxFemaleScore, femaleScoreDict, countryScoreDict = createScoreDict()


    print("Female winner:")
    for key in femaleScoreDict:

        if(femaleScoreDict[key][1] == maxFemaleScore):
            print(f"{key}, {femaleScoreDict[key][0]} - Score: {femaleScoreDict[key][1]}")

    countryScoreList = [countryScoreDict[key] for key in countryScoreDict]
    countryScoreList.sort()
    countryScoreList.reverse()
    print("Overall Rankings")
    num = 1
    for score in countryScoreList[0: 3]:
        for key in countryScoreDict:
            if(countryScoreDict[key] == score):
                print(f"{num}-) {key}-Final Score: {score}")
                num += 1

printAll()
