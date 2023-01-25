
# Height row column

# row = 0 and column = 0
# row = 0 and column = len(Matrix) -1
# row = len(matrix)-1 and column = 0
# row = len(matrix)-1 and column = len(matrix)-1

def readFile():

    fileFlag = True
    path = "map.txt"
    while(fileFlag):

        try:
            infile = open(path, "r")
            heightMatrix = []
            for line in infile:
                tempList = line.strip().split(" ")
                tempList = [int(x) for x in tempList]
                heightMatrix.append(tempList)
            infile.close()
            fileFlag = False

        except ValueError:
            path = input("Enter again the file path we couldn't find: ")

    return heightMatrix

def findPeak():

    heightMatrix = readFile()
    peakMatrix = []
    for row in range(len(heightMatrix)):

        for column in range(len(heightMatrix[row])):

            tempList = []
            if (row != 0 and column != len(heightMatrix) -1 and row != len(heightMatrix)-1 and column != 0):

                if(heightMatrix[row][column]> heightMatrix[row][column+1] and heightMatrix[row][column] > heightMatrix[row][column-1] and heightMatrix[row][column]> heightMatrix[row-1][column]
                and heightMatrix[row][column]> heightMatrix[row+1][column] and heightMatrix[row][column]> heightMatrix[row+1][column+1] and heightMatrix[row][column]> heightMatrix[row-1][column-1] and heightMatrix[row][column]> heightMatrix[row-1][column+1] and heightMatrix[row][column]> heightMatrix[row+1][column-1]):
                    tempList = [heightMatrix[row][column], row, column]

            else:

                if(row == 0 and column == 0 and heightMatrix[row][column] > heightMatrix[row+1][column] and heightMatrix[row][column] > heightMatrix[row][column+1] and heightMatrix[row][column] > heightMatrix[row+1][column+1]):
                    tempList = [heightMatrix[row][column], row, column]

                if(row == len(heightMatrix)-1 and column == 0 and heightMatrix[row][column] > heightMatrix[row][column+1] and heightMatrix[row][column] > heightMatrix[row-1][column] and heightMatrix[row][column] > heightMatrix[row-1][column+1]):
                    tempList = [heightMatrix[row][column], row, column]

                if(row == 0 and column == len(heightMatrix[row])-1 and heightMatrix[row][column] > heightMatrix[row][column-1] and heightMatrix[row][column] > heightMatrix[row+1][column] and heightMatrix[row][column] > heightMatrix[row+1][column-1]):
                    tempList = [heightMatrix[row][column], row, column]

                if(row == len(heightMatrix[row])-1 and column == len(heightMatrix[row])-1 and heightMatrix[row][column] > heightMatrix[row][column-1] and heightMatrix[row][column] > heightMatrix[row-1][column] and heightMatrix[row][column] > heightMatrix[row-1][column-1]):
                    tempList = [heightMatrix[row][column], row, column]


                if(row == 0 and (column != 0 or column != len(heightMatrix)-1) and heightMatrix[row][column] > heightMatrix[row][column-1] and heightMatrix[row][column] > heightMatrix[row][column+1] and heightMatrix[row][column] > heightMatrix[row+1][column-1] and heightMatrix[row][column] > heightMatrix[row+1][column] and heightMatrix[row][column] > heightMatrix[row+1][column+1]):
                    tempList = [heightMatrix[row][column], row, column]

                if(row == len(heightMatrix)-1 and (column != 0 or column != len(heightMatrix)-1) and heightMatrix[row][column] > heightMatrix[row][column-1] and heightMatrix[row][column] > heightMatrix[row][column+1] and heightMatrix[row][column] > heightMatrix[row-1][column-1] and heightMatrix[row][column] > heightMatrix[row-1][column] and heightMatrix[row][column] > heightMatrix[row-1][column+1]):
                    tempList = [heightMatrix[row][column], row, column]

                if(column == 0 and (row != 0 or row != len(heightMatrix)-1) and heightMatrix[row][column] > heightMatrix[row-1][column] and heightMatrix[row][column] > heightMatrix[row+1][column] and heightMatrix[row][column] > heightMatrix[row][column+1] and heightMatrix[row][column] > heightMatrix[row-1][column+1] and heightMatrix[row][column] > heightMatrix[row+1][column+1]):
                    tempList = [heightMatrix[row][column], row, column]

                if(column == len(heightMatrix)-1 and (row != 0 or row != len(heightMatrix)-1) and heightMatrix[row][column] > heightMatrix[row-1][column] and heightMatrix[row][column] > heightMatrix[row+1][column] and heightMatrix[row][column] > heightMatrix[row][column-1] and heightMatrix[row][column] > heightMatrix[row-1][column-1] and heightMatrix[row][column] > heightMatrix[row+1][column-1]):
                    tempList = [heightMatrix[row][column], row, column]


            if(len(tempList)>0): peakMatrix.append(tempList)

    averageHeight = 0
    for peak in peakMatrix:

        print(peak)
        averageHeight += peak[0]

    print(f"Average peak is {(averageHeight / len(peakMatrix))}m")

def main():
    findPeak()

if __name__ == "__main__":
    main()
