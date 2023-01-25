

def readFile():


    fileFlag = True
    filePath = "glucometers.txt"

    while(fileFlag):

        try:
            infile = open(filePath, "r")
            lineList = infile.readlines()
            infile.close()
            fileFlag = False
        except OSError:
            print("we couldn't find the file")
            filePath = input("Enter the file path again: ")

    return lineList

def dataToDict():

    lineList = readFile()
    dataDict = {}

    for element in lineList:

        cleanElementList = element.strip().split(" ")

        if(cleanElementList[0] in dataDict):

            if(int(cleanElementList[2]) >= 200):
                dataDict[cleanElementList[0]].append(cleanElementList[1: 3])
        else:
            if(int(cleanElementList[2]) >= 200):
                dataDict[cleanElementList[0]] = []
                dataDict[cleanElementList[0]].append(cleanElementList[1: 3])

    for key in dataDict:

        numOfExceeds = 0
        for element in dataDict[key]:
            if(int(element[1]) >= 200):
                numOfExceeds += 1

        dataDict[key].append(numOfExceeds)


    return dataDict


def printAll():

    dataDict = dataToDict()

    numOfExList = [dataDict[key][-1] for key in dataDict]
    numOfExList.sort()
    numOfExList.reverse()
    print(numOfExList)

    for num in numOfExList:

        for key in dataDict:
            if(dataDict[key][-1] == num):

                for i in range(0, len(dataDict[key]) - 1):
                    print(f"{key} {dataDict[key][i][0]} {dataDict[key][i][1]}")
        print()



def main():
    printAll()

if __name__ == "__main__":
    main()


