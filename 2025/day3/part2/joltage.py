from utils import load_input
import time

def processJoltage(joltageString): 
    highestFirstNumber = 0
    highestSecondNumber = 0

    indexOfFirstHighest = -1
    indexOfSecondHighest = -1

    tempJoltageString = joltageString[:-1]

    for char in tempJoltageString:
        num = int(char)
        
        if num > highestFirstNumber:
            highestFirstNumber = num
            indexOfFirstHighest = joltageString.index(char)
            
    # sub string to after the first highest number
    indexOfFirstHighest = joltageString.index(str(highestFirstNumber)) + 1
    subString = joltageString[indexOfFirstHighest:]

    print ("Sub String:", subString)
        
    for char in subString:
        num = int(char)
        if num > highestSecondNumber:
            highestSecondNumber = num
            indexOfSecondHighest = subString.index(char) + indexOfFirstHighest

    result = int(f"{highestFirstNumber}{highestSecondNumber}")

    # highlight the first number and second highest number in the string in green and red

    highlightedString = ""
    for i, char in enumerate(joltageString):
        if i == indexOfFirstHighest - 1:
            highlightedString += f"\033[92m{char}\033[0m"  # Green
        elif i == indexOfSecondHighest:
            highlightedString += f"\033[91m{char}\033[0m"  # Red
        else:
            highlightedString += char

    print("Joltage:", highlightedString, "-> Result:", result)

    return result

if __name__ == "__main__":
    start_time = time.time()
    joltageReading = load_input()
    result = 0
    for joltage in joltageReading:
        result += processJoltage(joltage)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Total joltage result from all readings:", result)
    print()
    print(f"\033[92m\nExecution time: {elapsed_time:.4f} seconds\033[0m")
    print()