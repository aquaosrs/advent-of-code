from utils import load_input

def loadBeamGrid():
    result = load_input()
    grid = []
    for row in result:
        grid.append(list(row))
    return grid

def drawBeamGrid(grid, rowToHighlight=None, colToHighlight=None):
    for i, row in enumerate(grid):
        outputRow = ''
        for j, cell in enumerate(row):
            if i == rowToHighlight and j == colToHighlight:
                outputRow += f'\033[92m{cell}\033[0m'  # Green color
            elif i == rowToHighlight and colToHighlight is None:
                outputRow += f'\033[93m{cell}\033[0m'  # Yellow color
            elif cell == 'S':
                outputRow += f'\033[91m{cell}\033[0m'  # Red color
            else:
                outputRow += cell
        print(outputRow)
    print()

def processBeamGrid(grid):
    splitCount = 0
    previousRow = None
    rowIndex = 0
    for row in grid:
        if previousRow is not None:
            cellIndex = 0
            for cell in row:
                previousCell = previousRow[cellIndex]
                if cell == '.':
                    if previousCell == 'S' or previousCell == '|':
                        row[cellIndex] = '|'
                elif cell == '^':
                    if previousCell == 'S' or previousCell == '|':
                        splitCount += 1
                        if cellIndex > 0:
                            row[cellIndex - 1] = '|'
                        if cellIndex < len(row) - 1:
                            row[cellIndex + 1] = '|'
                cellIndex += 1
        previousRow = row
        rowIndex += 1

    return splitCount
                

if __name__ == "__main__":
    beamGrid = loadBeamGrid()
    splitCount = processBeamGrid(beamGrid)

    drawBeamGrid(beamGrid)
    print(f"Split count: {splitCount}")