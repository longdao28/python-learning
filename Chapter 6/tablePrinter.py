#! python3

def printTable(tabledat):
    numOfColumns = len(tabledat)
    numOfRows = len(tabledat[0])
    maxLengthLists = []
    for list in tabledat:
        maxLength = 0
        for item in list:
            if len(item) > maxLength:
                maxLength = len(item)
        maxLengthLists.append(maxLength)
    print(maxLengthLists)

    for row in range(numOfRows):
        for column in range(numOfColumns):
            print(tabledat[column][row].rjust(maxLengthLists[column]), end=' ')
        print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)


