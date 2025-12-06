from utils import load_input


def loadInputAsColumns():
    result = load_input()
    columns = []
    for colIndex in range(len(result[0].split())):
        column = []
        for row in result:
            entries = row.split()
            column.append(entries[colIndex])
        columns.append(column)
    return columns


def mathsColumn(column):
    operation = column[-1]
    numbers = column[:-1]

    result = 0

    if operation == '*':
        product = 1
        for item in numbers:
            product *= int(item)
        result = product
    elif operation == '+':
        result = sum(int(item) for item in numbers)
    return result


if __name__ == "__main__":
    columns = loadInputAsColumns()
    result = 0
    for column in columns:
        result += mathsColumn(column)
    print("Final Result:", result)