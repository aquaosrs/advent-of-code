from utils import load_input
import time

def loadInputAsGrid():
    result = load_input()
    grid = []
    for row in result:
        grid.append(list(row))
    return grid

def printGrid(grid):
    for row in grid:
        outputRow = ''
        for cell in row:
            if cell == '.':
                outputRow += f'\033[90m{cell}\033[0m'  # Gray color
            elif cell == '@':
                outputRow += f'\033[92m{cell}\033[0m'  # Green color
        print(outputRow)
    print()

def printOutputGrid(grid):
    for row in grid:
        outputRow = ''
        for cell in row:
            if cell == '.':
                outputRow += f'\033[90m{cell}\033[0m'  # Gray color
            elif cell.isdigit():
                num = int(cell)
                if num > 3:
                    outputRow += f'\033[91m{cell}\033[0m'  # Red color
                else:
                    outputRow += f'\033[92m{cell}\033[0m'  # Green color
            else:
                outputRow += cell
        print(outputRow)
    print()

def printHighlightedGridWithRedCells(grid, rowToHighlight, colToHighlight, redCells):
    for i, row in enumerate(grid):
        outputRow = ''
        for j, cell in enumerate(row):
            if i == rowToHighlight and j == colToHighlight:
                outputRow += f'\033[92m{cell}\033[0m'  # Green color
            elif (i, j) in redCells:
                outputRow += f'\033[91m{cell}\033[0m'  # Red color
            else:
                outputRow += cell
        print(outputRow)
    print()


def calculateAdjacentCount(grid):
    # make a copy of the grid for the output
    output = [row[:] for row in grid]

    i, j = 0, 0
    for row in grid:
        j = 0
        for cell in row:

            if cell == '@':
                adjacentCellWithRollsCount = 0
                for direction in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]: # look at all 8 adjacent cells
                    newRow = i + direction[0]
                    newCol = j + direction[1]
                    if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(row):
                        if grid[newRow][newCol] == '@':
                            adjacentCellWithRollsCount += 1

                output[i][j] = str(adjacentCellWithRollsCount)
            j += 1
        i += 1
            
    return output

def removeRolls(grid):
    count = 0
    result = calculateAdjacentCount(grid)
    for i, row in enumerate(result):
        for j, cell in enumerate(row):
            if cell.isdigit() and int(cell) <= 3:
                grid[i][j] = '.'
                count += 1
    return grid, count

def removeRollsUntilStable(grid):
    totalRemoved = 0
    while True:
        grid, removedThisPass = removeRolls(grid)
        totalRemoved += removedThisPass
        if removedThisPass == 0:
            break
    return grid, totalRemoved

if __name__ == "__main__":
    start_time = time.time()
    grid = loadInputAsGrid()

    result, totalRemoved = removeRollsUntilStable(grid)
    printGrid(result)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print ("Total rolls removed:", totalRemoved)
    print(f"\033[92m\nExecution time: {elapsed_time:.4f} seconds\033[0m")
    