def getRange(rangeStr):
    start_str, end_str = rangeStr.split("-")
    start = int(start_str)
    end = int(end_str)
    return list(range(start, end + 1))

def isInvalid(productID):
    # Placeholder for actual validation logic
    return False

def processRange(rangeStr):
    rangeStr = rangeStr.strip()
    productRange = getRange(rangeStr)
    productCount = len(productRange)
    print(f"Processing range {rangeStr}: {productCount} products.")

    invalidIds = []

    for product in productRange:
        # Placeholder for actual product processing logic
        if isInvalid(product):
            print(f"Product {product} is invalid.")
            invalidIds.append(product)

    return invalidIds




if __name__ == "__main__":
    with open("2025/day2/Input.txt", "r") as f:
        productRanges = f.read().strip().split(",")
        
    for rangeStr in productRanges:
        products = processRange(rangeStr)
        print(f"Invalid products in range {rangeStr}: {products}")
        # Further processing can be done here