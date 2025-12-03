import time
from multiprocessing import Pool, cpu_count

def getRange(rangeStr):
    start_str, end_str = rangeStr.split("-")
    start = int(start_str)
    end = int(end_str)
    return list(range(start, end + 1))

def isInvalid(productID):
    idStr = str(productID)
    lengthOfProductId = len(idStr)
    
    for checkLength in range(1, lengthOfProductId // 2 + 1):
        if checkIfDuplicatingForLength(productID, checkLength):
            return True
    return False

def checkIfDuplicatingForLength(productID, checkLength = 2):
    idStr = str(productID)
    lengthOfProductId = len(idStr)
    if lengthOfProductId < checkLength * 2:
        return False

    allParts = [idStr[i:i+checkLength] for i in range(0, lengthOfProductId, checkLength)]

    # if all parts are the same, return True
    firstPart = allParts[0]
    for part in allParts[1:]:
        if part != firstPart:
            return False
        
    return True


def processRange(rangeStr):
    rangeStr = rangeStr.strip()
    productRange = getRange(rangeStr)

    invalidIds = []

    for product in productRange:
        if isInvalid(product):
            invalidIds.append(product)

    return invalidIds


if __name__ == "__main__":
    start_time = time.time()

    with open("2025/day2/Input.txt", "r") as f:
        productRanges = f.read().strip().split(",")
        
    allInvalidProducts = []

    # for rangeStr in productRanges:
    #     invalidProducts = processRange(rangeStr)
    #     print(f"Invalid products in range {rangeStr}: {invalidProducts}")
    #     allInvalidProducts.extend(invalidProducts)

    with Pool(cpu_count()) as pool:
        results = pool.map(processRange, [r.strip() for r in productRanges])
    for rangeStr, invalidProducts in zip([r.strip() for r in productRanges], results):
        print(f"Invalid products in range {rangeStr}: {invalidProducts}")
        allInvalidProducts.extend(invalidProducts)

    print(f"Total invalid products found: {len(allInvalidProducts)}")
    totalInvalidSum = sum(allInvalidProducts)
    print(f"Sum of all invalid product IDs: {totalInvalidSum}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time

# color green for execution time
print(f"\033[92m\nExecution time: {elapsed_time:.4f} seconds\033[0m")
print()
    