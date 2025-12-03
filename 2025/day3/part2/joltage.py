from utils import load_input
import time

def highlightSelectedDigits(joltageString, selectedIndices):
    colors = [
        "\033[92m",  # Green
        "\033[91m",  # Red
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
        "\033[97m",  # White
        "\033[38;5;99m",   # Purple
        "\033[38;5;208m",  # Orange
        "\033[38;5;213m",  # Pink
        "\033[38;5;46m",   # Bright Green
        "\033[38;5;226m",  # Bright Yellow
    ]
    
    dimGray = "\033[38;5;240m"  # dark gray
    
    highlightedString = ""
    for i, char in enumerate(joltageString):
        if i in selectedIndices:
            batteryIndex = selectedIndices.index(i)
            colorCode = colors[batteryIndex % len(colors)]
            highlightedString += f"{colorCode}{char}\033[0m"
        else:
            highlightedString += f"{dimGray}{char}\033[0m"
    
    return highlightedString

def processJoltage(joltageString, numberOfBatteriesToTurnOn = 12): 
    highestNumbers = [0] * numberOfBatteriesToTurnOn
    highestIndices = [-1] * numberOfBatteriesToTurnOn

    for i in range(numberOfBatteriesToTurnOn):
        charIndexToStartFrom = 0
        if i > 0:
            charIndexToStartFrom = highestIndices[i - 1] + 1

        tempJoltageString = joltageString[charIndexToStartFrom:len(joltageString) - (numberOfBatteriesToTurnOn - i - 1)]
        j = charIndexToStartFrom
        for char in tempJoltageString:
            num = int(char)
            if num > highestNumbers[i]:
                highestNumbers[i] = num
                highestIndices[i] = j
            j += 1

    resultString = ''.join(str(num) for num in highestNumbers)
    result = int(resultString)

    highlightedString = highlightSelectedDigits(joltageString, highestIndices)

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