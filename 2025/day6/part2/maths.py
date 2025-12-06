from utils import load_input

def getColumns(): 
    result = load_input()

    output = []

    columns = []
    
    numCols = (len(result[0]) + 1)
    for colIndex in range(numCols):
        column = []
        for row in result:
            start = colIndex * 1
            end = start + 1
            column.append(row[start:end].strip())
        columns.append(column)

    # Columns: [['1', '', '', '*'], ['2', '4', '', ''], ['3', '5', '6', ''], ['', '', '', ''], ['3', '6', '9', '+'], ['2', '4', '8', ''], ['8', '', '', ''], ['', '', '', ''], ['', '3', '2', '*'], ['5', '8', '1', ''], ['1', '7', '5', ''], ['', '', '', ''], ['6', '2', '3', '+'], ['4', '3', '1', ''], ['', '', '4', ''], ['', '', '', '']]

    groupedColumns = []
    currentGroup = []
    for col in columns:
        if all(cell == '' for cell in col):
            if currentGroup:
                groupedColumns.append(currentGroup)
                currentGroup = []
        else:
            currentGroup.append(col)
    if currentGroup:
        groupedColumns.append(currentGroup)

    # groupedColumns: Grouped Columns: [[['1', '', '', '*'], ['2', '4', '', ''], ['3', '5', '6', '']], [['3', '6', '9', '+'], ['2', '4', '8', ''], ['8', '', '', '']], [['', '3', '2', '*'], ['5', '8', '1', ''], ['1', '7', '5', '']], [['6', '2', '3', '+'], ['4', '3', '1', ''], ['', '', '4', '']]]

    for group in groupedColumns:
        outputColumn = []
        operator = None
        for row in group:
            row = [cell for cell in row if cell != '']
            if row and row[-1] in ['*', '+']:
                operator = row[-1]
                # remove operator from row
                row = row[:-1]
            number = ''.join(row[:])
            outputColumn.append(number)
        if operator:
            outputColumn.append(operator)
            
        output.append(outputColumn)

    # Output:  [['1', '24', '356', '*'], ['369', '248', '8', '+'], ['32', '581', '175', '*'], ['623', '431', '4', '+']]

    return output

def loadInputAsColumns():
    columns = getColumns()

    outputCols = []

    for col in columns:
        outputCols.append(preProcessColumn(col))

    print ("Pre-processed Columns:", outputCols)

    return outputCols

def preProcessColumn(column):
    return column

def mathsColumn(column):
    operation = column[-1]
    numbers = column[:-1]

    result = 0

    if operation == '*':
        product = 1
        for item in numbers:
            product *= int(item)
        result = product
    elif operation == '+':
        result = sum(int(item) for item in numbers)
    return result


if __name__ == "__main__":
    columns = loadInputAsColumns()
    result = 0
    for column in columns:
        result += mathsColumn(column)
    print("Final Result:", result)