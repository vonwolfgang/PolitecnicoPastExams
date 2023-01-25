



def readFile(path):


    fileFlag = True
    while(fileFlag):

        try:
            infile = open(path, "r", encoding="UTF-8")
            lineList = infile.readlines()
            infile.close()
            fileFlag = False
        except OSError:
            print("we couldn't find the file")
            path = input("Enter again the path of the file: ")

    return lineList

def createDicts():

    productLineList = readFile("products.txt")
    purchasesLineList = readFile("purchases.txt")

    productDict = {}
    purchasesDict = {}

    for element in productLineList:
        cleanElementList = element.strip().split(" ")

        if(cleanElementList[0] not in productDict):
            productDict[cleanElementList[0]] = cleanElementList[1]

    for element in purchasesLineList:

        cleanElementList = element.strip().split(" ")

        if(cleanElementList[0] not in purchasesDict):

            purchasesDict[cleanElementList[0]] = []
            purchasesDict[cleanElementList[0]].append(cleanElementList[1])

        else:
            purchasesDict[cleanElementList[0]].append(cleanElementList[1])


    return productDict, purchasesDict


def findAndPrintSuspicious():

    productDict, purchasesDict = createDicts()

    suspiciousDict = {}

    for purchasesKey in purchasesDict:

        if(len(purchasesDict[purchasesKey]) > 1):

            suspiciousDict[purchasesKey] = purchasesDict[purchasesKey]

        elif(purchasesDict[purchasesKey][0] != productDict[purchasesKey]):

            suspiciousDict[purchasesKey] = purchasesDict[purchasesKey]

    print("Suspicious transactions list\n")

    for susKey in suspiciousDict:

        print(f"Product code: {susKey}\n"
            f"Official dealer: {productDict[susKey]}\n"
            "Dealer list:", end=" ")

        for dealer in suspiciousDict[susKey]:
            print(dealer, end=" ")

        print("\n")

def main():
    findAndPrintSuspicious()

if __name__ == "__main__":
    main()
























