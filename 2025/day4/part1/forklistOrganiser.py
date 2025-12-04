from utils import load_input

def loadInputAsGrid():
    result = load_input()
    grid = []
    for row in result:
        grid.append(list(row))
    return grid

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




def calculateSafePickups(grid):
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

if __name__ == "__main__":
    grid = loadInputAsGrid()

    result = calculateSafePickups(grid)
    printOutputGrid(result)

    safePickupCount = 0
    for row in result:
        for cell in row:
            if cell.isdigit() and int(cell) <= 3:
                safePickupCount += 1

    print("Number of safe pickups (3 or fewer adjacent forks):", safePickupCount)
    