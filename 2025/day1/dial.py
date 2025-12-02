

currentNumber = 50
currentTimesWeStopAtZero = 0

MAX_NUMBER = 99

def turnDial(steps):
    global currentNumber, currentTimesWeStopAtZero
    currentNumber = (currentNumber + steps) % (MAX_NUMBER + 1)

    if currentNumber == 0:
        currentTimesWeStopAtZero += 1

    return currentNumber

def turnDialFromString(stepsStr):
    # stepsStr is like this L10 or R15
    direction = stepsStr[0]
    steps = int(stepsStr[1:])
    if direction == 'L':
        return turnDial(-steps)
    elif direction == 'R':
        return turnDial(steps)
    else:
        raise ValueError("Invalid direction; must be 'L' or 'R'.")
    




if __name__ == "__main__":
    currentNumber = 50
    print(f"The dial starts by pointing at {currentNumber}.")
    # load from input.txt
    stepsList = []
    with open("2025/day1/Input.txt", "r") as f:
        for line in f:
            stepsList.append(line.strip())

    # line count
    print(f"Total lines read: {len(stepsList)}")
    
    for steps in stepsList:
        newNumber = turnDialFromString(steps)
        print(f"The dial is rotated {steps} to point at {newNumber}.")
        # log to a file
        with open("2025/day1/Output.log", "a") as log_file:
            log_file.write(f"The dial is rotated {steps} to point at {newNumber}.\n")
    
    print (f"Total times stopped at zero: {currentTimesWeStopAtZero}")
    

