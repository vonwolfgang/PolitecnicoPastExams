
def readZodiacCreatDict():

    isTrue = True
    filePath = "zodiaco.csv"
    while(isTrue):

        try:
            infile = open(filePath, "r")
            isTrue = False

        except FileNotFoundError:
            print("we couldn't find the file")
            filePath = input("Please enter again the path of the zodiac file: ")

    zodiacDict = {}

    for index, line in enumerate(infile):

        lineList = line.strip().split(",")
        tempList = []

        try:

            startList = lineList[1].split("/")
            startInDays = int(startList[0]) + (int(startList[1]) * 30)
            stopList = lineList[2].split("/")
            stopInDays = int(stopList[0]) + (int(stopList[1]) * 30)
        except ValueError:
            exit(f"File includes something in wrong format in this line {index + 1}.\n"
                 f"Fix this line {index + 1}. Program will be closed")

        tempList = [x for x in range(startInDays, stopInDays+1)]

        if lineList[0] not in zodiacDict : zodiacDict[lineList[0]] = tempList

    infile.close()

    return zodiacDict

def readSportiviCreatDict():

    isTrue = True
    filePath = "sportivi.csv"
    while(isTrue):

        try:
            infile = open(filePath, "r")
            isTrue = False

        except FileNotFoundError:
            print("we couldn't find the file")
            filePath = input("Please enter again the path of the zodiac file: ")

    bornInDaysScoreMatrix = []

    for index, line in enumerate(infile):

        tempList = []
        lineList = line.strip().split(",")

        try:

            bornDateList = lineList[3].split("/")
            bornDateInDays = int(bornDateList[0]) + (int(bornDateList[1]) * 30)

        except ValueError:
            exit(f"File includes something in wrong format in this line {index + 1}.\n"
                 f"Fix this line {index + 1}. Program will be closed")

        tempList.append(bornDateInDays)
        tempList.append(int(lineList[1]))
        bornInDaysScoreMatrix.append(tempList)

    infile.close()

    return bornInDaysScoreMatrix

def createZodiacScore():

    zodiacDict = readZodiacCreatDict()
    bornInDaysScoreMatrix = readSportiviCreatDict()

    finalDict = {}

    for key in zodiacDict:

        for element in bornInDaysScoreMatrix:

            if(key not in finalDict and element[0] in zodiacDict[key]):
                finalDict[key] = element[1]

            elif(key in finalDict and element[0] in zodiacDict[key]):
                finalDict[key] += element[1]

    return finalDict

def printZodiacAndScore():

    finalDict = createZodiacScore()
    copyFinalDict = dict(finalDict)

    onlyXValue = 50 / max(finalDict.values())
    print(finalDict)
    while(len(copyFinalDict.keys()) > 0):

        currentMax = max(copyFinalDict.values())

        for key in finalDict:
            if(key in copyFinalDict and copyFinalDict[key] == currentMax):
                asterix = "*" * int(onlyXValue * copyFinalDict[key])
                print(f"{key : <15} {asterix}")
                copyFinalDict.pop(key)


def main():
    printZodiacAndScore()
if __name__ == "__main__":
    main()

