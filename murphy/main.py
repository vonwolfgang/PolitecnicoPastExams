
from string import punctuation

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
            path = input("enter again the path of the file, because we couldn't find: ")

    return lineList


def murphyDict():

    murphyLineList = readFile("Murphy_reads.txt")
    murphyDict = {}
    flag = True
    for elem in murphyLineList:

        if(elem != ""):
            if(flag):
                title = elem
                murphyDict[title] = []
                flag = False
            murphyDict[title].append(elem)
        elif(elem == ""):
            flag = True

    cleanMurphydict = {}

    for key in murphyDict:

        cleanMurphydict[key] = []
        for element in murphyDict[key]:

            elementList = element.split(" ")
            tempList = []

            for word in elementList:
                cleanWord = word.strip(punctuation)
                lowerCleanWord = cleanWord.lower()
                tempList.append(lowerCleanWord)
            cleanMurphydict[key].append(tempList)

    return murphyDict, cleanMurphydict

def printAllShown():

    murpDict, cleanMurpDict = murphyDict()
    argumentList = readFile("arguments.txt")

    for argument in argumentList:

        for key in cleanMurpDict:

            for index, element in enumerate(cleanMurpDict[key]):

                if((argument in element or argument in key) and len(murpDict[key][index]) <= 50):

                    print(f"{key} - {murpDict[key][index]}")

                elif((argument in element or argument in key) and len(murpDict[key][index]) > 50):

                    print(f"{key} - {murpDict[key][index][ :51]}...")



def main():
    printAllShown()

if __name__ == "__main__":
    main()


