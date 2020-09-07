tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    ncols=len(tableData)
    nrows=len(tableData[0])
    colWidths=[0]*ncols
    for i in range(ncols):
        longestWord=0
        for j in range(nrows):
            longestWord=max(longestWord, len(tableData[i][j]))
        colWidths[i]=longestWord

    for x in range(0,nrows):
        for y in range(0,ncols):
            print(tableData[y][x].rjust(colWidths[y])+' ', end='')
        print()

printTable(tableData)

