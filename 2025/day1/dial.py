

currentNumber = 50
currentTimesWePassedZero = 0
currentTimesWeStopAtZero = 0

MAX_NUMBER = 99

def turnDial(steps):
    global currentNumber, currentTimesWePassedZero, currentTimesWeStopAtZero
    currentNumber = (currentNumber + steps)

    if steps > MAX_NUMBER or steps < -MAX_NUMBER:
        wrap_count, normalized = divmod(currentNumber, MAX_NUMBER + 1)
        currentNumber = normalized
        currentTimesWePassedZero += abs(wrap_count)

    if currentNumber > MAX_NUMBER:
        currentNumber = currentNumber - (MAX_NUMBER + 1)
        currentTimesWePassedZero += 1
    elif currentNumber < 0:
        currentNumber = (MAX_NUMBER + 1) + currentNumber
        currentTimesWePassedZero += 1

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
    stepsList = []
    with open("2025/day1/Input.txt", "r") as f:
        for line in f:
            stepsList.append(line.strip())

    print(f"Total lines read: {len(stepsList)}")
    
    for steps in stepsList:
        newNumber = turnDialFromString(steps)
        print(f"The dial is rotated {steps} to point at {newNumber}.")
        with open("2025/day1/Output.log", "a") as log_file:
            log_file.write(f"The dial is rotated {steps} to point at {newNumber}.\n")
    
    print (f"Total times passed zero: {currentTimesWePassedZero}")
    print (f"Total times stopped at zero: {currentTimesWeStopAtZero}")
    
