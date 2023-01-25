

from string import punctuation


def readFileCreateMatrix():

    isTrue = True
    filePath = input("Enter the file path: ")

    while(isTrue):

        try:
            infile = open(filePath, "r")
            isTrue = False

        except FileNotFoundError:
            print("We couldn't find the file")
            filePath = input("Enter the file path again: ")

    cleanLineWordsMatrix = []

    for line in infile:

        cleanLineList = line.strip().split(" ")

        for word in cleanLineList:

            if(word != " " and word!=""):
                cleanLineWordsMatrix.append(word.strip(punctuation))


    return cleanLineWordsMatrix


def findTriplets():

    wordsMatrix = readFileCreateMatrix()
    listOfTupleOfTriplets = []

    for index in range(1, len(wordsMatrix) - 1):

        first = wordsMatrix[index - 1]
        second = wordsMatrix[index]
        third = wordsMatrix[index + 1]

        if(len(first) == len(second) and len(first) == len(third)):

            tupleTemp = (first.upper(), second.upper(), third.upper())
            listOfTupleOfTriplets.append(tupleTemp)

    for triplet in listOfTupleOfTriplets:

        print(triplet)



if __name__ == "__main__":
    findTriplets()




