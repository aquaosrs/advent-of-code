from utils import load_input
import time

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

def drawBeamGridTimeline(gridTimeline, rowToHighlight=None, colToHighlight=None):
    for t, grid in enumerate(gridTimeline):
        print(f"Time: {t}")
        drawBeamGrid(grid, rowToHighlight, colToHighlight)

def isAboveBeam(cell):
    return cell == 'S' or cell == '|'

def processBeamGrid(grid):
    height = len(grid)

    timelineGrids = [grid]

    timelineGridsToBeAddedOnNextIteration = []

    for heightLevel in range(height):
        if heightLevel == 0:
            continue  # skip the top level
        timelineGrids.extend(timelineGridsToBeAddedOnNextIteration)
        timelineGridsToBeAddedOnNextIteration = []

        start_time = time.time()

        # for each cell in the row
        for timeLineGrid in timelineGrids:
            for j, cell in enumerate(timeLineGrid[heightLevel]):
                if isAboveBeam(timeLineGrid[heightLevel - 1][j]):
                    if cell == '.':
                        timeLineGrid[heightLevel][j] = '|'
                    elif cell == '^':
                        newTimelineGrid = [row[:] for row in timeLineGrid]
                        # in the current timeline grid, make the beam go left
                        if j > 0:
                            timeLineGrid[heightLevel][j - 1] = '|'
                        # in the new timeline grid, make the beam go right
                        if j < len(newTimelineGrid[heightLevel]) - 1:
                            newTimelineGrid[heightLevel][j + 1] = '|'
                            # add the new timeline grid to the list of timeline grids
                            timelineGridsToBeAddedOnNextIteration.append(newTimelineGrid)
        
        elapsed_time = time.time() - start_time
        print(f"Processing height level {heightLevel}/{height} - completed in {elapsed_time:.3f} seconds")
    
    return len(timelineGrids)
    
                

if __name__ == "__main__":
    # clear the terminal
    print("\033c", end="")
    print ("Beam Grid Analysis")
    beamGrid = loadBeamGrid()
    timelineGrids = processBeamGrid(beamGrid)
    print(f"Timeline counts: {timelineGrids}")