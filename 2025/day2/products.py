def getRange(rangeStr):
    start_str, end_str = rangeStr.split("-")
    start = int(start_str)
    end = int(end_str)
    return list(range(start, end + 1))

def isInvalid(productID):
    idStr = str(productID)
    lengthOfProductId = len(idStr)
    if lengthOfProductId % 2 == 1:
        return False

    firstHalf = idStr[:lengthOfProductId // 2]
    secondHalf = idStr[lengthOfProductId // 2:]

    if firstHalf == secondHalf:
        print(f"Product ID {productID} is invalid (both halves are equal).")
        return True
    return False

def processRange(rangeStr):
    rangeStr = rangeStr.strip()
    productRange = getRange(rangeStr)
    productCount = len(productRange)
    print(f"Processing range {rangeStr}: {productCount} products.")

    invalidIds = []

    for product in productRange:
        if isInvalid(product):
            print(f"Product {product} is invalid.")
            invalidIds.append(product)

    return invalidIds




if __name__ == "__main__":
    with open("2025/day2/Input.txt", "r") as f:
        productRanges = f.read().strip().split(",")
        
    allInvalidProducts = []

    for rangeStr in productRanges:
        invalidProducts = processRange(rangeStr)
        print(f"Invalid products in range {rangeStr}: {invalidProducts}")
        allInvalidProducts.extend(invalidProducts)

    print(f"Total invalid products found: {len(allInvalidProducts)}")
    totalInvalidSum = sum(allInvalidProducts)
    print(f"Sum of all invalid product IDs: {totalInvalidSum}")