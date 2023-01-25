

def readFile():

    fileFlag = True
    filePath = "bowling.txt"

    while(fileFlag):

        try:
            infile = open(filePath, "r")
            lineList = infile.readlines()
            infile.close()
            fileFlag = False
        except OSError:
            print("we couldn't find the file")
            filePath = input("enter the file name again: ")
    print(lineList)
    return lineList

def score():

    lineList = readFile()

    scoreDict = {}
    numOfTenDict = {}
    numOfZeroDict = {}

    for line in lineList:

        nameScoreList = line.strip().split(";")

        surname = nameScoreList[0]
        name = nameScoreList[1]
        tempList = nameScoreList[2: ]

        try:
            tempList = [int(x) for index, x in enumerate(tempList)]
        except ValueError:
            exit("There is something which is in wrong format in the file")

        numOfTen = 0
        numOfZero = 0

        for x in tempList:
            if x == 10 :
                numOfTen += 1
            elif x == 0:
                numOfZero += 1

        fullName = f"{name} {surname}"

        scoreDict[fullName] = sum(tempList)
        numOfTenDict[fullName] = numOfTen
        numOfZeroDict[fullName] = numOfZero

    return scoreDict, numOfTenDict, numOfZeroDict

dictMan = {}


def printAll():

    scoreDict, numOfTenDict, numOfZeroDict = score()
    decoyScoreDict = dict(scoreDict)

    for key in scoreDict:

        currentMax = max(decoyScoreDict.values())

        for key2 in scoreDict:

            if(scoreDict[key2] == currentMax):

                print(f"{key2} {scoreDict[key2]}")
                decoyScoreDict.pop(key2)

    numOfTenMax = max(numOfTenDict.values())
    for keyTen in numOfTenDict:

        if(numOfTenDict[keyTen] == numOfTenMax):

            print(f"{keyTen} has knocked down all the pins {numOfTenMax} times")


    numOfZeroMax = max(numOfZeroDict.values())
    for keyZero in numOfZeroDict:

        if(numOfZeroDict[keyZero] == numOfZeroMax):

            print(f"{keyZero} has missed all the pins {numOfZeroMax} time (s)")



def main():
    printAll()


if __name__ == "__main__":
    main()




