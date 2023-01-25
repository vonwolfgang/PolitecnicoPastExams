


def readFileCreateMatrix():

    fileFlag = True

    while(fileFlag):

        try:
            fileName = input("Enter file name: ")
            infile = open(fileName, "r")
            fileFlag = False
        except FileNotFoundError:
            print("We couldn't find the file please enter valid file name")

    contentMatrix = []

    for line in infile:

        contentMatrix.append(line.strip("\n"))

    return contentMatrix

def coordinatsControl():

    contentMatrix = readFileCreateMatrix()

    isTrue = True
    while(isTrue):

        isTrue = False

        x = int(input("PLease enter the x coordinat: "))
        y = int(input("PLease enter the y coordinat: "))
        n = int(input("PLease enter the size of the square: "))

        for i in range(y, y+n):

            try:
                contentMatrix[i][x+n]
                contentMatrix[i][x]
            except IndexError:
                print("These coordinates is not inside the picture please enter new coordinates")
                isTrue = True
                break

    return x, y, n, contentMatrix


def createRequestedMatrix():

    x, y, n, contentMatrix = coordinatsControl()

    requestedMatrix = []

    for i in range(y, y+n):

        requestedMatrix.append(contentMatrix[i][x : x+n])

    return requestedMatrix

def calculatePercentageAndPrintRequestedMatrix():

    requestedMatrix = createRequestedMatrix()
    totalNumChar = len(requestedMatrix[0]) * len(requestedMatrix)
    print("The part of the figure to analyze is")
    for element in requestedMatrix:
        print(element)

    numOfCharDict = {}

    for element in requestedMatrix:

        for character in element:

            if character in numOfCharDict:

                numOfCharDict[character] += 1

            else:

                numOfCharDict[character] = 1


    for key in numOfCharDict:

        currentPercentage = (numOfCharDict[key] / totalNumChar) * 100
        numOfCharDict[key] = str(currentPercentage) + "%"


    for key in sorted(numOfCharDict):

        print(f"{key} ---> {numOfCharDict[key]}")





calculatePercentageAndPrintRequestedMatrix()







