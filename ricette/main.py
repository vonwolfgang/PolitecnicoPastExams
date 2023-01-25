
from string import punctuation

def readFile(path):

    fileFlag = True

    while(fileFlag):

        try:
            infile = open(path, "r")
            lineList = []
            for line in infile:
                lineList.append(line.strip())
            infile.close()
            fileFlag = False
        except OSError:
            path = input("Enter again the file path we couldn't find: ")

    return lineList

def createDicts():

    fusilliList = readFile("fusilli_alle_olive.txt")[1: ]
    polentaList = readFile("polenta_concia.txt")[1: ]
    foodList = readFile("foods.txt")

    fusilliDict = {}
    polentaDict = {}
    foodDict = {}

    for elem in foodList:

        elemList = elem.split(";")
        elemList = [x.strip(" ") for x in elemList]
        foodDict[elemList[0]] = []
        foodDict[elemList[0]].append(float(elemList[1]) / 1000)
        foodDict[elemList[0]].append(int(elemList[2]) / 1000)

    for elem in fusilliList:

        if elem == "":
            break
        elemList = elem.split(";")
        elemList = [x.strip(" ") for x in elemList]
        fusilliDict[elemList[0]] = int(elemList[1])

    for elem in polentaList:

        if elem == "":
            break
        elemList = elem.split(";")
        elemList = [x.strip(" ") for x in elemList]
        polentaDict[elemList[0]] = int(elemList[1])

    return foodDict, polentaDict, fusilliDict

def printAll():

    foodDict, polentalDict, fusilliDict = createDicts()

    totalCost = 0
    totalCalori = 0

    print("Igredients: ")
    for ingred in polentalDict:

        try:
            print(f"{ingred} - {polentalDict[ingred]}")
            totalCost += foodDict[ingred][0] * polentalDict[ingred]
            totalCalori += foodDict[ingred][1] * polentalDict[ingred]
        except KeyError:
            print(f"There is no food as {ingred} in food's file")
            continue

    print("\n")
    print(f"Number of Ingredients: {len(polentalDict)}")
    print(f"Recipe cost: {totalCost}")
    print(f"Recipe calories: {totalCalori}\n")

    totalCost = 0
    totalCalori = 0
    print("Igredients: ")
    for ingred in fusilliDict:

        try:
            print(f"{ingred} - {fusilliDict[ingred]}")
            totalCost += foodDict[ingred][0] * fusilliDict[ingred]
            totalCalori += foodDict[ingred][1] * fusilliDict[ingred]
        except KeyError:
            print(f"There is no food as {ingred} in food's file")
            continue
    print("\n")
    print(f"Number of Ingredients: {len(fusilliDict)}")
    print(f"Recipe cost: {totalCost}")
    print(f"Recipe calories: {totalCalori}")

def main():
    printAll()

if __name__ == "__main__":
    main()





















