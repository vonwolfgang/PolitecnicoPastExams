
def readFile(path):

    fileFlag = True
    filePath = path
    while(fileFlag):

        try:
            infile = open(filePath, "r")
            lineList = infile.readlines()
            infile.close()
            fileFlag = False

        except OSError:
            print("We couldn't find the file")
            filePath = input("Enter the file path again: ")


    return lineList


def songDict():

    lineList = readFile("artists.txt")

    artistDict = {}

    for line in lineList:

        cleanLineList = line.strip().split(";")
        bandCode = cleanLineList[0]
        bandFilePath = cleanLineList[1]

        bandFileList = readFile(bandFilePath)

        tempList = []

        for dateSong in bandFileList:

            tempList.append(dateSong.strip().split(";"))

        artistDict[bandCode] = tempList

    return artistDict

def printAll():

    artistDict = songDict()

    yearSet = set()

    for artist in artistDict:

        for song in artistDict[artist]:

            yearSet.add(int(song[0]))

    for year in sorted(yearSet):

        print(f"{year}: ")

        for artist1 in artistDict:

            for songs in artistDict[artist1]:

                try:
                    if(int(songs[0]) == year):
                        print(f"{songs[1] : <30} {artist1}")
                except ValueError:
                    exit("file includes something in wrong format program will closed")


def main():
    printAll()

if __name__ == "__main__":
    main()












