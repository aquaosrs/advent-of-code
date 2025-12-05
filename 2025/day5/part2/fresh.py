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

def combine_ranges(ranges):
    if not ranges:
        return []

    ranges.sort(key=lambda x: x[0])
    combined = [ranges[0]]

    for current in ranges[1:]:
        last = combined[-1]
        if current[0] <= last[1] + 1:
            combined[-1] = (last[0], max(last[1], current[1])) 
        else:
            combined.append(current)

    return combined


if __name__ == "__main__":
    freshIds = load_ranges()

    print ("Fresh ID Range Count:", len(freshIds))

    combinedFreshIds = combine_ranges(freshIds)

    print ("Combined Fresh ID Range Count:", len(combinedFreshIds))

    countOfFreshIds = 0
    for start, end in combinedFreshIds:
        countOfFreshIds += (end - start + 1)

    print ("Total FRESH products:", countOfFreshIds)