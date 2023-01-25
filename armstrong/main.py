
import math


def readFileCreateList():

    filePath = "numbers.txt"
    fileFlag = True

    while(fileFlag):

        try:
            inFile = open(filePath, "r")
            fileFlag = False
        except FileNotFoundError:
            print("We couldn't find the file")
            filePath = input("please enter a valid file path: ")

    numList = []
    for line in inFile:
        numList.append(line.strip())

    inFile.close()

    return numList

def findTheArmstrongs():

    numList = readFileCreateList()
    armstrongList = []

    for strNum in numList:

        numOfDigits = len(strNum)
        sum = 0
        try:
            intNum = int(strNum)
        except ValueError:
            exit("Sorry file inclueds wrong format. Program will be closed")

        while(intNum > 0):

            singDigit = intNum % 10
            sum += (pow(singDigit, numOfDigits))
            intNum = intNum // 10

        if(sum == int(strNum)):
            armstrongList.append((strNum+"\n"))

    return armstrongList

def writeArmstrong():

    armstrongList = findTheArmstrongs()

    outFile = open("armstrongFile.txt", "w")


    for num in armstrongList:

        outFile.write(num)

    outFile.close()


if __name__ == '__main__':
    writeArmstrong()











