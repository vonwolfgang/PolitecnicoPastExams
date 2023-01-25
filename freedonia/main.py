



""" BURDA SILME ISLEMINDE BIR SORUN VAR """

def readRulesCreateDict():

    isTrue = True
    filePath = "rules.dat.tt"
    while(isTrue):

        try:
            infile = open(filePath, "r")
            isTrue = False
        except FileNotFoundError:
            print("We couldn't find the file")
            filePath = input("Please enter the true path of rules file: ")

    rulesDict = {}
    for line in infile:

        lineList = line.strip().split(" ")
        lineList[0] = lineList[0].strip(":")

        dateList = lineList[0].split("-")

        try:
            dateValueDays = int(dateList[0]) + (int(dateList[1]) * 30) + (int(dateList[2]) * 365)
        except ValueError:
            exit("The file includes something in wrong format program will be closed")

        rulesDict[dateValueDays] = lineList[1: ]

    infile.close()

    return rulesDict


def readDatesCreateList():

    isTrue = True
    filePath1 = "dates."
    while(isTrue):

        try:
            infile = open(filePath1, "r")
            isTrue = False
        except FileNotFoundError:
            print("We couldn't find the file")
            filePath1 = input("Please enter the true path of rules file: ")

    datesListInDays = []

    for line in infile:

        cleanLine = line.strip()
        dateList = cleanLine.split("-")

        try:
            dateValueInDays = int(dateList[0]) + (int(dateList[1]) * 30) + (int(dateList[2]) * 365)
            datesListInDays.append(dateValueInDays)

        except ValueError:
            exit("The file includes something in wrong format program will be closed")


    infile.close()

    return datesListInDays

def createUpdatedRulesDict(datesList, rulesDict):


    #datesList = readDatesCreateList()
    #rulesDict = readRulesCreateDict()

    updatedRulesDict = {}

    for dateRequested in sorted(datesList):

        for rulesDate in sorted(rulesDict):

            if(dateRequested not in updatedRulesDict):

                updatedRulesDict[dateRequested] = []

                if(rulesDate < dateRequested):
                    for element in rulesDict[rulesDate]:

                        if(element[0] == "+"):
                            updatedRulesDict[dateRequested].append(element)

                elif(rulesDate > dateRequested):

                    for element in rulesDict[rulesDate]:
                        if(element[0] == "-" and element in updatedRulesDict[dateRequested]):
                            updatedRulesDict[dateRequested].remove(element)

            else:
                if(rulesDate < dateRequested):
                    for element in rulesDict[rulesDate]:
                        if(element[0] == "+"):
                            updatedRulesDict[dateRequested].append(element)

                elif(rulesDate > dateRequested):
                    for element in rulesDict[rulesDate]:
                        if(element[0] == "-" and element in updatedRulesDict[dateRequested]):
                            updatedRulesDict[dateRequested].remove(element)


    return updatedRulesDict


def printTheUpdatedRulesDict(updatedRulesDict):

    #updatedRulesDict = createUpdatedRulesDict()

    for key in updatedRulesDict:

        year = key // 365
        month = (key % 365) // 30
        day = ((key % 365) % 30)

        print("*" * 50)
        print(f"{day}-{month}-{year}\n")

        for value in updatedRulesDict[key]:
            print(value[1: ])
        print("*" * 50)

rulesDict = readRulesCreateDict()
print(f"Rules Dict {rulesDict}")
datesList = readDatesCreateList()
print(f"Dates list {datesList}")

updatedRulesDict = createUpdatedRulesDict(datesList, rulesDict)
print(f"Updated Rules Dict {updatedRulesDict}")

printTheUpdatedRulesDict(updatedRulesDict)



