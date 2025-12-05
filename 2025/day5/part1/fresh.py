from utils import load_input

def load_ranges():
    result = load_input()
    ranges = []
    reading_ranges = True
    for line in result:
        if line == '':
            reading_ranges = False
            continue
        if reading_ranges:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
    return ranges

def loadProductIds():
    result = load_input()
    numbers = []
    reading_numbers = False
    for line in result:
        if line == '':
            reading_numbers = True
            continue
        if reading_numbers:
            numbers.append(int(line))
    return numbers

def isInRange(value, ranges):
    for start, end in ranges:
        if start <= value <= end:
            return True
    return False


if __name__ == "__main__":
    freshIds = load_ranges()
    productIds = loadProductIds()
    print ("Fresh IDs:", freshIds)
    print ("Product IDs:", productIds)

    freshCount = 0

    for productId in productIds:
        if isInRange(productId, freshIds):
            freshCount += 1

    print ("Total FRESH products:", freshCount)