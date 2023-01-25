


def readFile(path):

    fileFlag = True
    while(fileFlag):

        try:
            infile = open(path, "r", encoding="UTF-8")
            lineList = []

            for line in infile:
                lineList.append(line.strip())
            infile.close()
            fileFlag = False

        except OSError:
            path = input("We couldn't find the file enter again the file path: ")

    return lineList

def createDicts():

    charList = readFile("characters.txt")
    questList1 = readFile("question1.txt")
    questList2 = readFile("question2.txt")

    headerList = charList[0].split(";")
    characDict = {}

    for character in charList[1: ]:

        tempDict = {}
        elementList = character.split(";")

        for index in range(1, len(elementList)):

            tempDict[headerList[index]] = elementList[index]

        characDict[elementList[0]] = tempDict

    questDict1 = {}
    for quest in questList1:

        tempList = quest.split("=")
        tempList = [x.strip(" ") for x in tempList]
        questDict1[tempList[0]] = tempList[1]

    questDict2 = {}
    for quest in questList2:

        tempList = quest.split("=")
        tempList = [x.strip(" ") for x in tempList]
        questDict2[tempList[0]] = tempList[1]

    return questDict1, questDict2, characDict

def printCharacDict(characDict):
    for speci in characDict:
        print(f"{speci} - ", end=" ")
        for key in characDict[speci]:
            print(f"{key}: {characDict[speci][key]}", end=" ")
        print("")


def guessWho(questDict, characDict):

    decoyCharacDict = dict(characDict)

    print("Game characters: ")
    printCharacDict(decoyCharacDict)
    print()
    step = 1
    for questKey in questDict:

        print(f"Step {step} - question: {questKey} = {questDict[questKey]}\n")

        for charac in characDict:

            if(charac in decoyCharacDict and decoyCharacDict[charac][questKey] != questDict[questKey]):
                decoyCharacDict.pop(charac)

        printCharacDict(decoyCharacDict)
        print("\n")
        step += 1

    if(len(decoyCharacDict) == 1):
        print(f"Congratulations, you win! Character selected: ")
        printCharacDict(decoyCharacDict)
    else:
        print("Too bad, you lose")


def main():

    questDict1, questDict2, characDict = createDicts()
    guessWho(questDict2, characDict)

if __name__ == "__main__":
    main()

















