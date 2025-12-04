from utils import load_input


def isRowSafe(rowString):
    parts = rowString.split(' ')
    lastPart = None
    increasing = None

    errorCount = 0

    for part in parts:        
        if lastPart is not None:
            diff = int(part) - int(lastPart)
            

            if(diff == 0 or abs(diff) > 3):
                errorCount += 1
            
            if increasing is not None:
                if(diff > 0 and not increasing):
                    errorCount += 1
                elif(diff < 0 and increasing):
                    errorCount += 1

            if(diff > 0):
                increasing = True
            elif(diff < 0):
                increasing = False
        lastPart = part

    return errorCount == 0 or errorCount == 1


if __name__ == "__main__":
    result = load_input()
    safeCount = 0
    for row in result:
        safe = isRowSafe(row)
        print("Row safe:", safe)
        if safe:
            safeCount += 1
    print("Number of safe rows:", safeCount)