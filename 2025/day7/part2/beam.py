from utils import load_input

def loadBeamGrid():
    result = load_input()
    grid = []
    for row in result:
        grid.append(list(row))
    return grid

def convertToMathsFormat(originalGrid):
    # Start position
    start_pos = None
    for i, row in enumerate(originalGrid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start_pos = (i, j)
                break
        if start_pos:
            break

    # Identify splits
    splits = []
    for i, row in enumerate(originalGrid):
        for j, cell in enumerate(row):
            if cell == '^':
                splits.append((i, j))
    
    levels = {}
    levels[0] = {start_pos[1]: 1}  # Start with 1 timeline at starting column
    
    for row_index in range(len(originalGrid) - 1):
        next_row = originalGrid[row_index + 1]
                    
        next_level = {}
        
        for col, timeline_count in levels[row_index].items():
            next_cell = next_row[col]
            
            if next_cell == '^':
                left_col = col - 1
                right_col = col + 1
                if left_col >= 0:
                    next_level[left_col] = next_level.get(left_col, 0) + timeline_count
                if right_col < len(next_row):
                    next_level[right_col] = next_level.get(right_col, 0) + timeline_count
            elif next_cell == '.' or next_cell == '|':
                # Continue straight down
                next_level[col] = next_level.get(col, 0) + timeline_count
        
        if next_level:
            levels[row_index + 1] = next_level
    
    return {
        'start': start_pos,
        'splits': splits,
        'levels': levels,
        'num_splits': len(splits)
    }

def calculateTimelinesFromMaths(maths_format):    
    max_level = max(maths_format['levels'].keys())
    final_level = maths_format['levels'][max_level]
    
    total = sum(final_level.values())
    return total

if __name__ == "__main__":
    originalGrid = loadBeamGrid()    
    mathsFormat = convertToMathsFormat(originalGrid)
    
    print(f"\nStarting position: {mathsFormat['start']}")
    print(f"Total splits: {mathsFormat['num_splits']}")
    print(f"\nTimeline progression by level (row):")
    print("------------------------------------------------")
    
    for level in sorted(mathsFormat['levels'].keys()):
        positions = mathsFormat['levels'][level]
        total_at_level = sum(positions.values())
        print(f"Row {level:2d}: {total_at_level:4d} timelines at columns {dict(positions)}")
    
    totalTimelines = calculateTimelinesFromMaths(mathsFormat)
    print("\n==============================================================")
    print(f"TOTAL UNIQUE TIMELINES: {totalTimelines}")
    print("==============================================================")
    